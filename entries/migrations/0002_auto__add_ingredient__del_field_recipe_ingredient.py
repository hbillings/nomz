# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Ingredient'
        db.create_table('entries_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.Recipe'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('ingredient', self.gf('django.db.models.fields.CharField')(max_length=600)),
        ))
        db.send_create_signal('entries', ['Ingredient'])

        # Deleting field 'Recipe.ingredient'
        db.delete_column('entries_recipe', 'ingredient')


    def backwards(self, orm):
        
        # Deleting model 'Ingredient'
        db.delete_table('entries_ingredient')

        # Adding field 'Recipe.ingredient'
        db.add_column('entries_recipe', 'ingredient', self.gf('django.db.models.fields.CharField')(default=datetime.date(2011, 10, 4), max_length=200), keep_default=False)


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
            'message': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['entries']
