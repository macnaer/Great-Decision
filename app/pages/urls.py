from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('we_offer', views.we_offer, name="we_offer"),
    path('apartment', views.apartment, name="apartment"),
]
