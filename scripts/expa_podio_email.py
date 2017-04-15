# encoding:utf-8
from __future__ import unicode_literals
from datetime import datetime, timedelta
from django.template import Template, Context
from django_podio import api, tools
from django_documents import documentsApi
from django_mailTemplates import mailApi
import pdb

def email_document(item, expa_podio_email_hook, podioApi):
    """
    This method takes a PODIO item, retrieves its data, and uses it to fill out fields inside an odt/pdf document template and/or an email. The document will be sent as an attachment of the email, if both exist.
    """
    ans = ""
    hook = expa_podio_email_hook
    
    #Guarda los transformadores de variable simples
    transformer_dict = {}
    #Guarda los transformadores de variable complejos
    related_transformer_dict = {}
    transformers = hook.transformers.all()
    attachments = []
    #Distribuye los transformadores presentes entre simples y complejos
    for transformer in transformers:
        if "#" in transformer.key: #Es un valor que está adentro de un Related Item
            related_transformer_dict[transformer.key] = transformer.value
        else:
            transformer_dict[int(transformer.key)] = transformer.value
    data = tools.dictSwitch(item['values'], transformer_dict, related_transformer_dict, True)#Crea el diccionario final, que será utilizado en los templates de los correos o de los pdfs, a partir de el item de PODIO y los distintos valores

    #TODO: Qué hace esto?
    flat_data = tools.flatten_dict(data)

    #Para reemplazar las variables de tipo fecha
    for date in hook.dates.all():
        #Primero se revisa si la fecha es un valor de PODIO o la fecha actual
        if date.field_id == "":
            raw_date = datetime.today() 
        else:
            raw_date = datetime.strptime(item['values'][int(date.field_id)]['value']['start_date'], "%Y-%m-%d")
            #TODO Debe atender dos casos: cuando es un campo normal y cuando es un campo dentro de un related item
        #Segundo, se corre la fecha la cantidad de días que especifica el date_manager
        raw_date = raw_date + timedelta(days=date.time_delta)
        #Tercero, se define el formato que va a tomar la fecha
        if date.formatting == date.INGLES:
            formatter = "%d of %B, %Y" 
        elif date.formatting == date.ESPANHOL:
            mes = tools.MESES[int(raw_date.strftime("%m")) - 1]
            formatter = "%d de " + mes + ", %Y"
        elif date.formatting == date.DMA:
            formatter = "%d/%m/%Y"
        elif date.formatting == date.DIA:
            formatter = "%d"
        elif date.formatting == date.MES:
            mes = tools.MESES[int(raw_date.strftime("%m")) - 1]
            formatter = mes
        elif date.formatting == date.MONTH:
            formatter = "%B"
        elif date.formatting == date.NUM_MES:
            formatter = "%m"
        elif date.formatting == date.ANHO:
            formatter = "%Y"
        #Al final, se agrega el valor de la variable al diccionario
        print date.variable
        flat_data[date.variable] = raw_date.strftime(formatter)
            
    flat_data['fecha'] = datetime.today().strftime('%d de %%s, %Y') % tools.MESES[int(datetime.today().strftime('%m')) - 1]
    print flat_data

    #Aplica si existe un template de correo que se envía automáticamente
    if hook.email_template:
        print "Iniciando el envio del correo"
        print hook.email_template.pk
        email = mailApi.MailApi(hook.email_template.name)
        from_email = tools.retrieve_email(hook.from_email, item)
        to_email = tools.retrieve_email(hook.to_email, item)
        if hook.cc_email:
            cc_email = tools.retrieve_email(hook.cc_email, item)
        else:
            cc_email = []
        print "Enviando correo a %s desde %s" % (to_email, from_email)
        email_send_status = "Test mode"
        try:
            email_send_status = str(email.send_mail(from_email, [to_email], flat_data, attachments=attachments))
        except Exception as e:
            email_send_status = "ERROR enviando el correo" 
        print "Status de envio: %s" % email_send_status
        status += email_send_status
    print "Ejecucion exitosa del hook"
    return status
        
