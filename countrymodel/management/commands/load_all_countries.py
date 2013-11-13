#-*- coding:utf-8 -*-

from  django.core.management.base import BaseCommand

from countrymodel import CountryModel

from django_countries.countries import COUNTRIES


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """
        Loads all countries from django_countries as a record on the database.
        """
        for country in COUNTRIES:
            c = CountryModel(country=country[0])
            c.save()
