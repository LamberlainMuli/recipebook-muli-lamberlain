from django.shortcuts import render
import json

RECIPE_LIST_PATH = "ledger/databases/Recipe List Context.txt"
RECIPES_PATH = "ledger/databases/recipes"

def recipe_list(request):
    #import from databases/Recipe List Context 
    recipe_list_text = open(RECIPE_LIST_PATH,encoding='utf-8')   
    #transform to json (dictionary)
    recipe_list_context = json.load(recipe_list_text)   
    return render(request, "recipe_list.html", recipe_list_context)

def get_recipe(request, recipe_id):
    #import from databases/recipes/Recipe <id>
    recipe_text = open(f'{RECIPES_PATH}/Recipe {recipe_id}.txt',encoding='utf-8')   
    #transform to json (dictionary)
    recipe_context = json.load(recipe_text)   
    return render(request, "recipe.html", recipe_context)