from django.contrib import admin
from .models import Category, Product

# register the model product.
admin.site.register(Product)

# register the model Category.
admin.site.register(Category)

