# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CountryModel'
        db.create_table('countrymodel_countrymodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django_countries.fields.CountryField')(unique=True, max_length=2)),
        ))
        db.send_create_signal('countrymodel', ['CountryModel'])


    def backwards(self, orm):
        # Deleting model 'CountryModel'
        db.delete_table('countrymodel_countrymodel')


    models = {
        'countrymodel.countrymodel': {
            'Meta': {'object_name': 'CountryModel'},
            'country': ('django_countries.fields.CountryField', [], {'unique': 'True', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['countrymodel']
