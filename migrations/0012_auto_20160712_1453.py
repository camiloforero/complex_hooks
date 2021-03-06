# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-12 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complex_hooks', '0011_auto_20160712_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datemanager',
            name='time_delta',
            field=models.IntegerField(default=0, help_text='La cantidad de dias que se debe correr la fecha. Si es un momento en el pasado se pueden usar valores negativos', verbose_name='Dias de diferencia'),
        ),
        migrations.AlterField(
            model_name='datemanager',
            name='variable',
            field=models.CharField(help_text='El valor dentro de los PDFs o correos electr\xf3nicos que ser\xe1 reemplazado por esta fecha', max_length=32, verbose_name='Variable'),
        ),
    ]
