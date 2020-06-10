from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Apartments


def index(request):
    apartments = Apartments.objects.order_by(
        "-list_date").filter(is_publish=True)

    paginator = Paginator(apartments, 5)
    page = request.GET.get('page')
    pagged_apartments = paginator.get_page(page)
    context = {
        'apartments': pagged_apartments
    }
    return render(request, "pages/apartments.html", context)


def apartment(request, apartment_id):
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    context = {
        "apartment": apartment
    }
    return render(request, 'pages/apartment.html', context)


def search(request):
    estate_list = Apartments.objects.order_by(
        "-list_date").filter(is_publish=True)

    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            estate_list = estate_list.filter(city__iexact=city)

    print(estate_list)
    context = {
        'estate_list': estate_list
    }
    return render(request, 'pages/search.html', context)
