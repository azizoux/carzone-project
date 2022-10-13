from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from cars.models import Car


def cars(request):
    cars = Car.objects.order_by('-created_date')
    search_fields = {
        'model': list(Car.objects.values_list('model', flat=True).distinct()),
        'year': list(Car.objects.values_list('year', flat=True).distinct()),
        'body_style': list(Car.objects.values_list('body_style', flat=True).distinct()),
        'city': list(Car.objects.values_list('city', flat=True).distinct()),
    }
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars': paged_cars,
        'search_fields': search_fields,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    search_fields = {
        'model': list(Car.objects.values_list('model', flat=True).distinct()),
        'year': list(Car.objects.values_list('year', flat=True).distinct()),
        'body_style': list(Car.objects.values_list('body_style', flat=True).distinct()),
        'city': list(Car.objects.values_list('city', flat=True).distinct()),
        'transmission': list(Car.objects.values_list('transmission', flat=True).distinct()),
    }

    if 'keyword' in request.GET and request.GET['keyword']:
        keyword = request.GET['keyword']
        cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET and request.GET['model']:
        model = request.GET['model']
        cars = cars.filter(model__iexact=model)

    if 'city' in request.GET and request.GET['city']:
        city = request.GET['city']
        cars = cars.filter(city__iexact=city)

    if 'body_style' in request.GET and request.GET['body_style']:
        body_style = request.GET['body_style']
        cars = cars.filter(body_style__iexact=body_style)

    if 'year' in request.GET and request.GET['year']:
        year = request.GET['year']
        cars = cars.filter(year__iexact=year)

    if 'transmission' in request.GET and request.GET['transmission']:
        transmission = request.GET['transmission']
        cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET and request.GET['max_price']:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'search_fields': search_fields,
    }
    return render(request, 'cars/search.html', data)
