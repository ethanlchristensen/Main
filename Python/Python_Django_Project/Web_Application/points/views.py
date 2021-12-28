from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import points_to_user
from users.models import *

def update_points(request):
    points = int(request.POST['points'])
    print(points)
    p = points_to_user.objects.get(user=request.user.username)
    p.points = p.points + points
    p.save()
    return redirect('main-home')
