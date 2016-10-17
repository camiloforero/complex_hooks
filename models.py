#coding:utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django_podio.models import Hook
from django_documents.models import ODTTemplate
from django_mailTemplates.models import Email
from django_expa.models import LoginData

from django.db import models

###################### PODIO - EMAIL -DOCUMENT ###################

@python_2_unicode_compatible
class EmailDocumentHook(models.Model):
    name = models.CharField("Nombre", help_text="Nombre del hook. Es bueno que sea descriptivo sin ser muy largo", max_length=64)
    description = models.TextField("Descripción", help_text="Descripción: Qué hace este hook exactamente?")
    hook = models.OneToOneField(Hook, models.CASCADE, null=True, blank=True, related_name = "email_document_hook", help_text="El hook de la aplicación y del item al cual está asociado este hook completo. EL módulo de dicho hook debe ser hook_email_document.py")
    document = models.ForeignKey(ODTTemplate, models.CASCADE, help_text="El documento que se generará automáticamente cada vez que se llama este hook. Es importante que los valores de los campos a llenar dentro de dicho documento hayan sido debidamente llenados con los field_id correspondientes de la aplicación de PODIO", blank=True, null=True)
    generate_odt = models.BooleanField("Documento en word?", help_text="Si se marca, el documento va a ser generado como un word en vez de un pdf, lo cual permitirá modificaciones adicionales", default=False)
    email_template = models.ForeignKey(Email, models.CASCADE, help_text="EL template del email que se le va a enviar a la persona.", blank=True, null=True)
    attach_document_to_item = models.BooleanField("Determina si el documento generado va a ser adjuntado al item de PODIO o no", default=True)
    from_email = models.CharField("Correo de envío", help_text="El correo desde el cual se envía el documento y el correo, o un valor numérico del field_id donde se puede encontrar", max_length=256)
    to_email = models.CharField("Destinatario", help_text="El correo electrónico del destinatario, o un valor numérico con el field_id donde se puede encontrar", max_length=256, blank=True, null=True)
    cc_email = models.CharField("El correo electrónico de un cc, o un valor numérico con el field_id donde se puede encontrar", max_length=256, blank=True, null=True)
    podio_user_client = models.BooleanField("Usar cuenta personal de PODIO?", help_text="Define si se va a correr el hook como la aplicación o como un usuario en específico. Algunas aplicaciones no tienen los permisos necesarios para leer un item en otro espacio de trabajo; en esos casos se utiliza la cuenta de usuario configurada por defecto", default=False)
    def __str__(self):
        return "Complex Hook: %s - %s - %s" % (self.hook, self.document, self.email_template)
        
    
@python_2_unicode_compatible
class Condition(models.Model):
    """
    Esta clase representa una condición sobre un campo que el hook complejo debe cumplir para activarse. Pueden haber una o más condiciones.
    """
    complex_hook = models.ForeignKey(EmailDocumentHook, models.CASCADE, help_text="El hook al cual pertenece esta condición", related_name="conditions")
    field_id = models.PositiveIntegerField("La field_id del campo sobre el cual se quiere configurar la condición")
    condition_type = models.CharField("El tipo de condición. En este momento este valor no importa, pero eventualmente habrá más tipos de condiciones", default="=", max_length=16)#TODO: Agregar acá un campo tipo choices
    value = models.CharField("El valor que debe tomar el campo seleccionado anteriormente para que este hook se dispare", max_length=32)
    def __str__(self):
        return "%s %s %s" % (self.field_id, self.condition_type, self.value)

@python_2_unicode_compatible
class Transformer(models.Model):
    """
    Esta clase representa los distintos transformadores que habrá sobre el hook complejo. Por ejemplo, si el campo "nombre" sale del field_id '1349384' entonces esta clase debe hacer el mapeo entre los dos
    """
    complex_hook = models.ForeignKey(EmailDocumentHook, models.CASCADE, help_text="El hook al cual pertenece este transformador", related_name="transformers")
    key = models.CharField("PODIO Field ID", help_text="El valor del field_id que será utilizado para reemplazar el campo en el correo o en el documento generado", max_length=32)
    value = models.CharField("Variable", help_text="El valor dentro del template del correo o el template del documento que será llenado con el campo del item de PODIO identificado con el field_id ingresado previamente", max_length=32)
    def __str__(self):
        return "%s:%s" % (self.key, self.value)

@python_2_unicode_compatible
class DateManager(models.Model):
    """
    Esta clase se utiliza para agregar campos que varían respecto a la fecha actual, y eventualmente respecto a un campo de fecha en PODIO, y darles distintos formatos (inglés, español, sólo el día o el mes).
    """
    INGLES = "ingles"
    ESPANHOL = "español"
    DMA = "dia/mes/año"
    DIA = "dia"
    MES = "mes"
    MONTH = "month"
    NUM_MES = "num_mes"
    ANHO = "año"
    FORMATOS = (
        (INGLES, "ingles"),
        (ESPANHOL, "español"),
        (DMA, "dia/mes/año"),
        (DIA, "dia"),
        (MES, "mes"),
        (MONTH, "month"),
        (NUM_MES, "num_mes"),
        (ANHO, "año"),
    )
    complex_hook = models.ForeignKey(EmailDocumentHook, models.CASCADE, help_text="El hook al que pertenece este campo de fecha", related_name="dates")
    field_id = models.CharField(help_text="El valor del field_id, de tipo fecha, que será utilizado como base para llenar este campo. Si está vacío, se utilizará la fecha actual", blank=True, null=True, max_length=32)
    variable = models.CharField("Variable", help_text="El valor dentro de los PDFs o correos electrónicos que será reemplazado por esta fecha", max_length=32)
    time_delta = models.IntegerField("Dias de diferencia", help_text="La cantidad de dias que se debe correr la fecha. Si es un momento en el pasado se pueden usar valores negativos", default=0)
    formatting = models.CharField("Formatos", help_text="Los formatos que puede tomar la fecha. Puede estar en inglés, en español, o en formato numérico", choices=FORMATOS, max_length=16)
    def __str__(self):
        return self.formatting + str(self.time_delta) + " dias"

######################### EXPA - PODIO - LOADER ###################

@python_2_unicode_compatible
class EXPAPodioLoader(models.Model):
    REGISTERED = 'registered'
    CONTACTED = 'contacted'
    APPLIED = 'applied'
    ACCEPTED = 'accepted'
    AN_SIGNED = 'an_signed'
    APPROVED = 'approved'
    REALIZED = 'realized'
    INTERACTIONS = (
        (REGISTERED, 'registered'),
        (CONTACTED, 'contacted'),
        (APPLIED, 'applied'),
        (ACCEPTED, 'accepted'),
        (AN_SIGNED, 'an_signed'),
        (APPROVED, 'approved'),
        (REALIZED, 'realized'),
    )
    OGV = 'ogv'
    OGIP = 'ogip'
    IGV = 'igv'
    IGIP = 'igip'
    OGX = 'ogx'
    ICX = 'icx'
    AREAS = (
        (OGV, 'ogv'),
        (OGIP, 'ogip'),
        (IGV, 'igv'),
        (IGIP, 'igip'),
        (OGX, 'ogx'),
        (ICX, 'icx'),
    )
    name = models.CharField("Nombre", help_text="Nombre del cargador a EXPA. es bueno que sea descriptivo sin ser muy largo", max_length=64)
    cuenta = models.ForeignKey(LoginData, models.PROTECT, help_text="La cuenta de EXPA que será utilizada para obtener el token de acceso")
    description = models.TextField("Descripción", help_text="Descripción: Qué hace este cargador exactamente?")
    interaction = models.CharField("Interacción", help_text="El tipo de interacción del usuario o de la oportunidad dentro de EXPA", choices=INTERACTIONS, max_length=16) 
    days_past = models.PositiveSmallIntegerField("Dias en el pasado", help_text="La cantidad de días en el pasado desde la que se desea solicitar los datos. Si es uno, se pedirán los de ayer.", default=1)
    lc_id = models.PositiveSmallIntegerField("LC ID", help_text="El EXPA ID del LC específico sobre el que se desea hacer la consulta.", default=1395)
    area = models.CharField("Area", help_text="El área sobre la cual se quiere hacer la consulta.", max_length=8, choices=AREAS)
    email_template = models.ForeignKey(Email, models.CASCADE, help_text="EL template del email que se le va a enviar a la persona, en caso que se desee", blank=True, null=True)
    from_email = models.CharField("Correo de envío", help_text="El correo desde el cual se envía el documento y el correo, o un valor numérico del field_id donde se puede encontrar", max_length=256)
    cc_email = models.CharField("El correo electrónico de un cc, o un valor numérico con el field_id donde se puede encontrar", max_length=256, blank=True, null=True)
    def __str__(self):
        return "Cargador EXPA-PODIO-Correo: %s - %s" % (self.name, self.email_template)
# Create your models here.
