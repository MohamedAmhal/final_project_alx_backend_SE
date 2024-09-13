from django.contrib import admin
from .models import Category, Product, Commande


# displaying the features in panal tables (for category table) :
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'added_date')


# displaying the features in panal tables (for product table) :
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'added_date')

# displaying the features in panal tables (for Commande table) :
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'zip', 'command_date')



# register the model product.
admin.site.register(Product, AdminProduct)

# register the model Category.
admin.site.register(Category, AdminCategory)

# register the model Commande.
admin.site.register(Commande, AdminCommande)