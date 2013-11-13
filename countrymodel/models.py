#-*- coding:utf-8 -*-

from django.db import models
from django_countries import CountryField


class CountryModel(models.Model):

    """Model wrapper around django_countries' CountryField."""

    country = CountryField(unique=True)

    @property
    def name(self):
        return self.country.name

    @property
    def code(self):
        return self.country.code

    @property
    def flag(self):
        return self.country.flag

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.code)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"
