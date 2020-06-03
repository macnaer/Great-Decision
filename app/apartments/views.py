from django.shortcuts import render
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
    return render(request, "pages/apartment.html", context)
