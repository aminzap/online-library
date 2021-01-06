from django.contrib import admin
from . import models


@admin.register(models.Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('name', 'pub_date','catToStr')

    def catToStr(self, obj):
        return ','.join([category.catName for category in obj.category.all()])

    catToStr.short_description = 'category'


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ('catName','parent', 'status')
