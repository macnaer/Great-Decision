from django.db import models
from datetime import datetime
from realtor.models import Realtor


class Apartments(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    rooms = models.IntegerField()
    square_live = models.DecimalField(max_digits=9, decimal_places=1)
    square_all = models.DecimalField(max_digits=9, decimal_places=1)
    floor = models.IntegerField()
    apartment_type = models.CharField(max_length=250)
    is_publish = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now)
    photo_0 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
