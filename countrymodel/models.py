from django.db import models
from django_countries import CountryField


class MultiCountry(models.Model):

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
        verbose_name = strings.COUNTRY
        verbose_name_plural = strings.COUNTRIES
