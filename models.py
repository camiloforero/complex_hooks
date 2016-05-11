#coding:utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django_podio.models import Hook
from django_documents.models import ODTTemplate
from django_mailTemplates.models import Email

from django.db import models

@python_2_unicode_compatible
class EmailDocumentHook(models.Model):
    name = models.CharField("Nombre del hook. Es bueno que sea descriptivo sin ser muy largo", max_length=64)
    description = models.TextField("Descripción: Qué hace este hook exactamente?")
    hook = models.OneToOneField(Hook, models.CASCADE, related_name = "email_document_hook", help_text="El hook de la aplicación y del item al cual está asociado este hook completo. EL módulo de dicho hook debe ser hook_email_document.py")
    document = models.ForeignKey(ODTTemplate, models.CASCADE, help_text="El documento que se generará automáticamente cada vez que se llama este hook. Es importante que los valores de los campos a llenar dentro de dicho documento hayan sido debidamente llenados con los field_id correspondientes de la aplicación de PODIO", blank=True, null=True)
    email_template = models.ForeignKey(Email, models.CASCADE, help_text="EL template del email que se le va a enviar a la persona.", blank=True, null=True)
    attach_document_to_item = models.BooleanField("Determina si el documento generado va a ser adjuntado al item de PODIO o no", default=True)
    from_email = models.CharField("El correo desde el cual se envía el documento y el correo, o un valor numérico del field_id donde se puede encontrar", max_length=256)
    to_email = models.CharField("El correo electrónico del destinatario, o un valor numérico con el field_id donde se puede encontrar", max_length=256, blank=True, null=True)
    cc_email = models.CharField("El correo electrónico de un cc, o un valor numérico con el field_id donde se puede encontrar", max_length=256, blank=True, null=True)
    def __str__(self):
        return "%s - %s - %s" % (self.hook, self.document, self.email_template)
        
    
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
    key = models.CharField("El valor del field_id que será utilizado para reemplazar el campo en el correo o en el documento generado", max_length=32)
    value = models.CharField("El valor dentro del template del correo o el template del documento que será llenado con el campo del item de PODIO identificado con el field_id ingresado previamente", max_length=32)
    def __str__(self):
        return "%s: %s:%s" % (self.complex_hook, self.key, self.value)

# Create your models here.
