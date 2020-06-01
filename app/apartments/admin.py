from django.contrib import admin

from .models import Apartments


class ApartmentsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "price", "is_publish")
    list_display_links = ("id", "title", "price")
    list_editable = ("is_publish",)
    search_fields = ("title", "price", "description")
    list_per_page = 30


admin.site.register(Apartments, ApartmentsAdmin)
