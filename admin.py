# coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import EmailDocumentHook, Condition, Transformer, DateManager

class ConditionInline(admin.TabularInline):
    model = Condition

class DateManagerInline(admin.TabularInline):
    model = DateManager

class TransformerInline(admin.TabularInline):
    model = Transformer

@admin.register(EmailDocumentHook)
class EmailDocumentHookAdmin(admin.ModelAdmin):
    list_display = ('name', 'hook', 'document', 'email_template')
    inlines = [
        ConditionInline,
        TransformerInline,
        DateManagerInline,
        ]
# Register your models here.
