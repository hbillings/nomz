from entries.models import Recipe
from entries.models import Ingredient
from django.contrib import admin

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 5

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['contributor']}),
        (None,               {'fields': ['instructions']}),
        ('Enter a personal message',               {'fields': ['message']}),
        ('Date added', {'fields': ['date_contributed']}),
    ]

admin.site.register(Recipe, RecipeAdmin)