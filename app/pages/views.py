from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    data = {"header_h1": "Про <span>Нас</span>",
            "header_p": "Головна >> Про нас"}
    return render(request, 'pages/about.html', context=data)


def we_offer(request):
    data = {"header_h1": "Що <span>Пропонуємо</span>",
            "header_p": "Головна >> Що пропонуємо"}
    return render(request, 'pages/we_offer.html', context=data)


def apartment(request):
    data = {"header_h1": " <span>Нерухомість</span>",
            "header_p": "Головна >> Нерухомість"}
    return render(request, 'pages/apartment.html', context=data)
