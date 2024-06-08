from car.models import Car
from brand.models import Brand
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def display_cars(request, brand_slug = None):
    data = Car.objects.all()
    brand = Brand.objects.all()
    if brand_slug is not None:
        single_brand = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(brand = single_brand)
    return render(request, 'home.html', {'data' : data, 'brand' : brand})