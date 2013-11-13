# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MultiCountry'
        db.create_table('countrymodel_multicountry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django_countries.fields.CountryField')(unique=True, max_length=2)),
        ))
        db.send_create_signal('countrymodel', ['MultiCountry'])


    def backwards(self, orm):
        # Deleting model 'MultiCountry'
        db.delete_table('countrymodel_multicountry')


    models = {
        'countrymodel.multicountry': {
            'Meta': {'object_name': 'MultiCountry'},
            'country': ('django_countries.fields.CountryField', [], {'unique': 'True', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['countrymodel']
