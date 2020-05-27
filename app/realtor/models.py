from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=70)
    email = models.EmailField(max_length=200, blank=False)
    city = models.CharField(max_length=100, blank=False)
    mvr = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now)
    birth_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
