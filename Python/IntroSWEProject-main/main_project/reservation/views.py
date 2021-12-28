from django.shortcuts import render, redirect
from .models import Reservation
from users.models import *
from django.contrib import messages
from restaurants.models import Restaurant

def home(request):
    context = {
        'reservations': Reservation.objects.all()
    }
    return render(request, 'reservation/home.html', context)


def profile(request):
    context = {
        'reservations': Reservation.objects.all()
    }
    return render(request, 'reservation/profile.html', context)


def about(request):
    return render(request, 'reservation/about.html', {'title': 'About'})


def make_reservation(request):
    if request.user.is_authenticated:
        context = {
            'restaurants': Restaurant.objects.all()
        }
        return render(request, 'reservation/make_reservation.html', context)
    else:
        messages.error(request, f'You must be logged in to make a reservation!')
        return redirect('login')


def add_reservation(request):
    x = request.POST['reservationName']
    y = request.POST['peopleCount']
    z = request.POST['tablePref']
    requests = request.POST['comments']
    date = request.POST['reservationTime']
    user = request.user.username
    res = request.POST['restaurants']
    new_item = Reservation(reservationName=x, peopleCount=y, boothTable=z, requests=requests, date=date, user=user, restaurant=res)
    new_item.save()
    return redirect('reservation-home')

