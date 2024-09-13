from django.urls import path
from shop.views import index, details, Checkout, confirmation

urlpatterns = [
    path('', index, name='Home'),
    path('<int:id_pro>', details, name='details'), #this url is dynamic one it change if the product change
    path('checkout', Checkout, name='checkout'),
    path('confirmation', confirmation, name='confirmation'),

]