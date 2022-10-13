from django.shortcuts import render
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    search_fields = {
        'model': list(Car.objects.values_list('model', flat=True).distinct()),
        'year': list(Car.objects.values_list('year', flat=True).distinct()),
        'body_style': list(Car.objects.values_list('body_style', flat=True).distinct()),
        'city': list(Car.objects.values_list('city', flat=True).distinct()),
        'transmission': list(Car.objects.values_list('transmission', flat=True).distinct()),
    }
    print("-" * 30)
    print(search_fields)
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'search_fields': search_fields,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
