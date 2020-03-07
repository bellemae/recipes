from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.

class Ingredient(models.Model):
    """Model representing an ingredient. eg. onion, tomato, etc"""
    name = models.CharField(max_length=20, help_text='Enter an ingredient')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Measurement(models.Model):
    """Model representing a type of measurement. eg. cup, teaspoon, gram, etc"""
    name = models.CharField(max_length=20, help_text='Enter a measurement type')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Category(models.Model):
    """Model representing a recipe category. eg. desert, snack, cake, salad etc"""
    name = models.CharField(max_length=20, help_text='Enter a recipe category')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Recipe(models.Model):
    """Model representing a recipe."""
    title = models.CharField(max_length=200)    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the recipe')
    
    # method = models.ManyToManyField(RecipeStep, help_text='Select a step for this method')
    category = models.ManyToManyField(Category, help_text='Select a category for this recipe')
    
    # attribution = models.CharField(max_length=40) 
    prep_time = models.IntegerField()
    recipe_yield = models.CharField(max_length=20)
    ## ADD a picture option


    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this recipe."""
        return reverse('recipe-detail', args=[str(self.id)])
    

class RecipeIngredient(models.Model):
    """Model representing an ingredient for a recipe. eg. onion, tomato, etc"""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(help_text='Enter an ingredient')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """String for representing the Model object."""
        if self.measurement:
            return str(self.quantity) + " " + str(self.measurement) + " " + str(self.ingredient)
        else:
            return str(self.quantity) + " " + str(self.ingredient)  


class RecipeStep(models.Model):
    position = models.IntegerField() # so each step is printed in order
    step = models.CharField(max_length=40, help_text='Enter the recipe step')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """String for representing the Model object."""
        return self.step

    class Meta:
        ordering = ['position']

class RecipeImage(models.Model):
    top_pic = models.BooleanField(default=False, help_text='Set if this is to be the top image')
    image_path = models.CharField(max_length=40, help_text='Enter the image url')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """String for representing the Model object."""
        return self.image_path