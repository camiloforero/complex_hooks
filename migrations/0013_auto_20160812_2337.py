# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-13 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complex_hooks', '0012_auto_20160712_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaildocumenthook',
            name='podio_user_client',
            field=models.BooleanField(default=False, help_text='Define si se va a correr el hook como la aplicaci\xf3n o como un usuario en espec\xedfico. Algunas aplicaciones no tienen los permisos necesarios para leer un item en otro espacio de trabajo; en esos casos se utiliza la cuenta de usuario configurada por defecto', verbose_name='Usar cuenta personal de PODIO?'),
        ),
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='description',
            field=models.TextField(help_text='Descripci\xf3n: Qu\xe9 hace este hook exactamente?', verbose_name='Descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='from_email',
            field=models.CharField(help_text='El correo desde el cual se env\xeda el documento y el correo, o un valor num\xe9rico del field_id donde se puede encontrar', max_length=256, verbose_name='Correo de env\xedo'),
        ),
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='name',
            field=models.CharField(help_text='Nombre del hook. Es bueno que sea descriptivo sin ser muy largo', max_length=64, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='to_email',
            field=models.CharField(blank=True, help_text='El correo electr\xf3nico del destinatario, o un valor num\xe9rico con el field_id donde se puede encontrar', max_length=256, null=True, verbose_name='Destinatario'),
        ),
    ]