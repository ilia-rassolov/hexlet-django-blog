from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category')
    search_fields = ['name', 'price', 'description', 'category']
    list_filter = (('category', DateFieldListFilter),)  # Перечисляем поля для фильтрации
