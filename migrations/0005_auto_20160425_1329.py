# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-25 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complex_hooks', '0004_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='hook',
            field=models.OneToOneField(help_text='El hook de la aplicaci\xf3n y del item al cual est\xe1 asociado este hook completo. EL m\xf3dulo de dicho hook debe ser hook_email_document.py', on_delete=django.db.models.deletion.CASCADE, related_name='email_document_hook', to='django_podio.Hook'),
        ),
    ]
