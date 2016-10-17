# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailTemplates', '0006_auto_20160513_1451'),
        ('django_expa', '0001_initial'),
        ('complex_hooks', '0014_emaildocumenthook_generate_odt'),
    ]

    operations = [
        migrations.CreateModel(
            name='EXPAPodioLoader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del cargador a EXPA. es bueno que sea descriptivo sin ser muy largo', max_length=64, verbose_name='Nombre')),
                ('description', models.TextField(help_text='Descripci\xf3n: Qu\xe9 hace este cargador exactamente?', verbose_name='Descripci\xf3n')),
                ('from_email', models.CharField(help_text='El correo desde el cual se env\xeda el documento y el correo, o un valor num\xe9rico del field_id donde se puede encontrar', max_length=256, verbose_name='Correo de env\xedo')),
                ('cc_email', models.CharField(blank=True, max_length=256, null=True, verbose_name='El correo electr\xf3nico de un cc, o un valor num\xe9rico con el field_id donde se puede encontrar')),
                ('cuenta', models.ForeignKey(help_text='La cuenta de EXPA que ser\xe1 utilizada para obtener el token de acceso', on_delete=django.db.models.deletion.PROTECT, to='django_expa.LoginData')),
                ('email_template', models.ForeignKey(blank=True, help_text='EL template del email que se le va a enviar a la persona, en caso que se desee', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_mailTemplates.Email')),
            ],
        ),
    ]