from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create the first view
def index(request):
    # display images in frontend
    # 1. select all prduct that exist in the database
    product_object = Product.objects.all()
    # 2. search items
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        #je vais un velo ==> velo display  so this is the objectif of itle__icontains
        product_object = Product.objects.filter(title__icontains = item_name)
    paginator = Paginator(product_object, 8)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object' : product_object})
