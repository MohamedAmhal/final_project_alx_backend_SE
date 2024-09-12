from django.shortcuts import render

# Create the first view
def index(request):
    return render(request, 'shop/index.html')
