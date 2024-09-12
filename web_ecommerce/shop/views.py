from django.shortcuts import render
from .models import Product

# Create the first view
def index(request):
    # display images in frontend
    # 1. select all prduct that exist in the database
    product_object = Product.objects.all()
    return render(request, 'shop/index.html', {'product_object' : product_object})
