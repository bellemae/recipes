from django.shortcuts import render
from catalog.models import Recipe, Ingredient, Category, RecipeIngredient
from django.views import generic

# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_recipes = Recipe.objects.all().count()
    num_ingredients = Ingredient.objects.all().count()
    num_categories = Category.objects.all().count()

    context = {
        'num_recipes': num_recipes,
        'num_ingredients': num_ingredients,
        'num_categories': num_categories
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by = 10

class RecipeDetailView(generic.DetailView):
    model = Recipe

    