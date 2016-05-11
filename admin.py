# coding=utf-8
from __future__ import unicode_literals
from django.contrib import admin
from .models import EmailDocumentHook, Condition, Transformer

class ConditionInline(admin.TabularInline):
    model = Condition

class TransformerInline(admin.TabularInline):
    model = Transformer

@admin.register(EmailDocumentHook)
class EmailDocumentHookAdmin(admin.ModelAdmin):
    list_display = ('name', 'hook', 'document', 'email_template')
    inlines = [
        ConditionInline,
        TransformerInline,
        ]
# Register your models here.
