# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-12 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complex_hooks', '0008_auto_20160425_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(blank=True, help_text='El valor del field_id, de tipo fecha, que ser\xe1 utilizado como base para llenar este campo. Si est\xe1 vac\xedo, se utilizar\xe1 la fecha actual', max_length=32, null=True)),
                ('time_delta', models.IntegerField(help_text='La cantidad de dias que se debe correr la fecha. Si es un momento en el pasado se pueden usar valores negativos', verbose_name='Dias de diferencia')),
                ('formatting', models.CharField(choices=[('ingles', 'ingles'), ('espa\xf1ol', 'espa\xf1ol'), ('dia/mes/a\xf1o', 'dia/mes/a\xf1o'), ('dia', 'dia'), ('mes', 'mes'), ('a\xf1o', 'a\xf1o')], help_text='Los formatos que puede tomar la fecha. Puede estar en ingl\xe9s, en espa\xf1ol, o en formato num\xe9rico', max_length=16, verbose_name='Formatos')),
                ('complex_hook', models.ForeignKey(help_text='El hook al que pertenece este campo de fecha', on_delete=django.db.models.deletion.CASCADE, related_name='dates', to='complex_hooks.EmailDocumentHook')),
            ],
        ),
    ]