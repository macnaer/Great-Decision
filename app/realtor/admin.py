from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "birth_date")
    list_display_links = ("id", "name", "email", "phone")
    list_per_page = 15


admin.site.register(Realtor, RealtorAdmin)
