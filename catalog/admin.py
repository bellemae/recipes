from django.contrib import admin
from .models import Ingredient, Measurement, RecipeIngredient, RecipeStep, Category, Recipe

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeStep)
admin.site.register(Category)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeStepInline(admin.TabularInline):
    model = RecipeStep


# Define the admin class
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeStepInline]

# Register the admin class with the associated model
admin.site.register(Recipe, RecipeAdmin)
