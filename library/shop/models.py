from django.db import models


class Shop(models.Model):
    city_choise = [('te', 'tehran'),
                   ('esf', 'esfehan'),
                   ('shz', 'shiraz'),
                   ('msd', 'mashad'),
                   ('tbz', 'tabriz'),
                   ('krm', 'kerman')]
    name = models.CharField(max_length=15)
    city_name = models.CharField(max_length=8,choices=city_choise)
    address = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
