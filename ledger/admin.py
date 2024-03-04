from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ['ingredient', 'recipe', 'quantity']
    list_filter = ['recipe']
    list_display = ['ingredient', 'recipe', 'quantity']

    fieldsets = [
        ('Details', {
            'fields' : [
                ('ingredient', 'recipe', 'quantity')
            ]
        })
    ]

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)