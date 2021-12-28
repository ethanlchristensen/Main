from django.shortcuts import render, redirect
from .models import Restaurant


def home(request):
    context = {
        'restaurants': Restaurant.objects.all()
    }
    return render(request, 'restaurants/restaurant.html', context)


def search(request):
    context = {
        'restaurants': Restaurant.objects.all()
    }
    return render(request, 'restaurants/search.html', context)


def post_search(request):
    res = request.POST['restaurants']
    restaurants = Restaurant.objects.all()
    for restaurant in restaurants:
        if restaurant.name == res:
            out = {"name": restaurant.name, "type": restaurant.type, "address": restaurant.address, "phone": restaurant.phone}
    return render(request, 'restaurants/post_search.html', out)


