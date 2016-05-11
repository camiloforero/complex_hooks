# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-22 17:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complex_hooks', '0002_auto_20160422_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='document',
            field=models.ForeignKey(blank=True, help_text='El documento que se generar\xe1 autom\xe1ticamente cada vez que se llama este hook. Es importante que los valores de los campos a llenar dentro de dicho documento hayan sido debidamente llenados con los field_id correspondientes de la aplicaci\xf3n de PODIO', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_documents.ODTTemplate'),
        ),
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='email_template',
            field=models.ForeignKey(blank=True, help_text='EL template del email que se le va a enviar a la persona.', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_mailTemplates.Email'),
        ),
    ]
