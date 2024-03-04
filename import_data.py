# Description: This script is used to import recipe data from txt files into the database
# Usage: python manage.py shell < recipebook-muli-lamberlain/import_data.py
from ledger.models import Recipe, Ingredient, RecipeIngredient
import json
import os

RECIPES_PATH = "ledger/databases/recipes"

for recipe in os.listdir(RECIPES_PATH):
    print(f'Processing {recipe}')
    # Open the recipe file
    recipe_text = open(f'{RECIPES_PATH}/{recipe}',encoding='utf-8')
    # Load the recipe details and convert to a dictionary
    recipe_details = json.load(recipe_text)
    # Create the recipe
    recipe = Recipe()
    recipe.name = recipe_details['name']
    # Save the recipe
    recipe.save()
    print(f'Created {recipe.name}')
    
    for ingredient_data in recipe_details['ingredients']:
        print(f'Processing {ingredient_data["name"]}')
        # Create the ingredient
        ingredient  = Ingredient()
        ingredient.name = ingredient_data['name']
        # Create the recipe ingredient
        recipe_ingredient = RecipeIngredient()
        recipe_ingredient.quantity = ingredient_data['quantity']
        recipe_ingredient.recipe = recipe
        recipe_ingredient.ingredient = ingredient
        # Save the ingredient and recipe ingredient
        ingredient.save()
        recipe_ingredient.save()
        print(f'Created {ingredient.name} - {recipe_ingredient.quantity}')