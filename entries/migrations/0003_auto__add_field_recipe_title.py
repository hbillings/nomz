# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Recipe.title'
        db.add_column('entries_recipe', 'title', self.gf('django.db.models.fields.CharField')(default=0, max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Recipe.title'
        db.delete_column('entries_recipe', 'title')


    models = {
        'entries.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entries.Recipe']"})
        },
        'entries.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'contributor': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_contributed': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['entries']
