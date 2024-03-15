from django.db import models
from django.urls import reverse
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Anonymous")
    created_on = models.DateTimeField(default=timezone.now, blank=True)
    updated_on = models.DateTimeField(default=timezone.now, blank=True)
    
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE, 
        related_name='ingredients'
    )

    def __str__(self):
        return f'{self.recipe.name} \t- {self.quantity} \t- {self.ingredient.name}'
