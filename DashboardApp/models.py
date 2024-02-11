from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='items')
    stock_status = models.FloatField() 
    available_stock = models.FloatField()
