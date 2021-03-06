# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-10 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complex_hooks', '0016_auto_20160819_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='hook',
            field=models.OneToOneField(blank=True, help_text='El hook de la aplicaci\xf3n y del item al cual est\xe1 asociado este hook completo. EL m\xf3dulo de dicho hook debe ser hook_email_document.py', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_document_hook', to='django_podio.Hook'),
        ),
    ]
