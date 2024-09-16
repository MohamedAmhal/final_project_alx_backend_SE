from django.contrib import admin
from .models import Category, Product, Commande, Reporte


#parameters of the admin page 
admin.site.site_header = "E-commerce Center"
admin.site.site_title = "Mohammed Shop"
admin.site.index_title = "Manadger"

# displaying the features in panal tables (for category table) :
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'added_date')
    search_fields = ('name', )


# displaying the features in panal tables (for product table) :
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'added_date')
    search_fields = ('title', )
    list_editable = ('price', 'category',)

# displaying the features in panal tables (for Commande table) :
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'address', 'city', 'total', 'command_date')
    search_fields = ('city', )
    list_editable = ('name', 'email', 'address', 'city', 'total',)


# displaying the features in panal tables (for Reporte table) :
class AdminReporte(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'added_date')
    search_fields = ('first_name', )



# register the model product.
admin.site.register(Product, AdminProduct)

# register the model Category.
admin.site.register(Category, AdminCategory)

# register the model Commande.
admin.site.register(Commande, AdminCommande)

# register the model Reporte.
admin.site.register(Reporte, AdminReporte)