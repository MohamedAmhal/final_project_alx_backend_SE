from django.shortcuts import render, redirect
from .models import Product, Commande, Category
from django.core.paginator import Paginator

# Create the first view
def index(request):
    # display images in frontend
    # 1. select all prduct that exist in the database
    product_object = Product.objects.all()
    cat =Category.objects.all()
    # 2. search items
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        #je vais un velo ==> velo display  so this is the objectif of itle__icontains
        product_object = Product.objects.filter(title__icontains = item_name)
    paginator = Paginator(product_object, 12)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object' : product_object, 'cat': cat})


# create the second veiw product details:
def details(request, id_pro):
    product_object = Product.objects.get(id = id_pro)
    return render(request, 'shop/details_product.html', {'product_object' : product_object})


# create the second veiw checkout:
def Checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('pays')
        zip = request.POST.get('zipcode')
        commande = Commande(items=items, total=total, name=name, email=email, address=address, city=city, country=country, zip=zip)
        commande.save()

        return redirect('confirmation')
    return render(request, 'shop/checkout.html')


# create the third veiw confirmation:

def confirmation(request):
    info = Commande.objects.all()[: 1]
    for item in info:
        name = item.name
    return render(request, 'shop/confirmation.html', {'name' : name})


# create the 5  view filtercategory:
def Filter_cat(request, id):
    cati = Category.objects.get(id=id)
    product = Product.objects.filter(category=cati)
    return render(request, 'shop/product_filter_category.html', {'product': product})


# create the 6 view about us page :
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')


