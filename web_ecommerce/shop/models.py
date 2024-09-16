from django.db import models
from django.db.models import ForeignKey

# class category

class Category(models.Model):
    name = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now=True)

    # creation du premier vue
    class Meta:
        ordering = ['-added_date']
    
    # pour voir les noms apparitres dans la table admin panal
    def __str__(self):
        return self.name


# class product
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    added_date = models.DateTimeField(auto_now=True)

    #creation du premier vue
    class Meta:
        ordering = ['-added_date']

    # pour voir les noms apparitres dans la table admin panal
    def __str__(self):
        return self.title


class Commande(models.Model):
    items = models.CharField(max_length=300, null=False, blank=False)
    total = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=300, null=False, blank=False)
    zip = models.CharField(max_length=300, null=False, blank=False)
    command_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-command_date']

    def __str__(self):
        return self.name


class Reporte(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=400, null=False, blank=False)
    message = models.CharField(max_length=800)
    added_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-added_date']

    def __str__(self):
        return self.first_name