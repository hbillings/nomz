# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Recipe'
        db.create_table('entries_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('instructions', self.gf('django.db.models.fields.TextField')()),
            ('contributor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_contributed', self.gf('django.db.models.fields.DateTimeField')()),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('entries', ['Recipe'])


    def backwards(self, orm):
        
        # Deleting model 'Recipe'
        db.delete_table('entries_recipe')


    models = {
        'entries.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'contributor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_contributed': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['entries']
