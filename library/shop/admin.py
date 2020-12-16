from django.contrib import admin
from . import models

@admin.register(models.Shop)
class AdminBook(admin.ModelAdmin):
    list_display = ['name','city_name']
