# <appname>/urls.py
from django.urls import path
from .views import recipe_list,get_recipe

urlpatterns = [ path('recipes/list', recipe_list, name='recipes list'),
                path('recipe/<str:recipe_id>', get_recipe, name='recipe details')]

app_name = "ledger"