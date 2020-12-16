from django.db import models
from shop.models import Shop


class Book(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    abstract = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    writer = models.CharField(max_length=25, null=True, blank=True)
    shop = models.ManyToManyField(Shop,  blank=True)
    category = models.ManyToManyField("Category")


class Category(models.Model):
    catName = models.CharField(max_length=15, verbose_name='category name')
    status = models.BooleanField(default=True, verbose_name='Do you want to show it?')

    def __str__(self):
        return self.catName
