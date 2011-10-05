from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField()
    contributor = models.CharField(max_length=200)
    date_contributed = models.DateTimeField('date published')
    message = models.TextField()
    def __unicode__(self):
            return self.title

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    amount = models.IntegerField()
    ingredient = models.CharField(max_length=600)
    def __unicode__(self):
            return self.ingredient