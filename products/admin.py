from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    # List of fields for disply in admin panel
    list_display = ["image_tag", "name", "category_to_str", "price", "stock"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # List of fields for disply in admin panel
    list_display = ['title', 'parent']
