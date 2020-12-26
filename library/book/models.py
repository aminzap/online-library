from django.db import models
from shop.models import Shop


class BookManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Book(models.Model):
    STATUS_CHOISES = (
        ('p', 'published'),
        ('d', 'draft'),
    )
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    abstract = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    writer = models.CharField(max_length=25, null=True, blank=True)
    shop = models.ManyToManyField(Shop, blank=True)
    category = models.ManyToManyField("Category", related_name='book')
    status = models.CharField(max_length=1, choices=STATUS_CHOISES, blank=True)


    def category_published(self):
        return self.category.filter(status=True)

    objects = BookManager()




class Category(models.Model):
    catName = models.CharField(max_length=15, verbose_name='category name')
    slug = models.SlugField(unique=True, max_length=50, null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='Do you want to show it?')

    def __str__(self):
        return self.catName
