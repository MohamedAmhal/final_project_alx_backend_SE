from django.db import models
from django.db.models import ForeignKey

# class category

class Category(models.Model):
    name = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now=True)

    #creation du premier vue
    class Meta:
        ord = ['-added_date']


# class product
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    added_date = models.DateTimeField(auto_now=True)

    #creation du premier vue
    class Meta:
        ord = ['-added_date']
