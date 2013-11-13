#-*- coding:utf-8 -*-

from django.contrib import admin


class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
