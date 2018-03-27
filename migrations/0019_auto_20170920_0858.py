# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-09-20 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complex_hooks', '0018_auto_20170804_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildocumenthook',
            name='name',
            field=models.CharField(help_text='Nombre del hook. Es bueno que sea descriptivo sin ser muy largo', max_length=64, verbose_name='Name'),
        ),
    ]