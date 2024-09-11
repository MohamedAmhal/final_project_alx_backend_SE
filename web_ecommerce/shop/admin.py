from django.contrib import admin
from .models import Category, Product


# displaying the features in panal tables (for category table) :
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'added_date')


# displaying the features in panal tables (for product table) :
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'added_date')


# register the model product.
admin.site.register(Product, AdminProduct)

# register the model Category.
admin.site.register(Category, AdminCategory)