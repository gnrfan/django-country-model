#-*- coding:utf-8 -*-

from django.contrib import admin


class MultiCountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
