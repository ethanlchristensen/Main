from django.shortcuts import render
from django.contrib.auth import get_user_model
from points.models import points_to_user

def home(request):
    User = get_user_model()
    context = {
        'users': User.objects.all(),
        'points': points_to_user.objects.all()
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, "main/about.html")

def stopwatch(request):
    return render(request, "main/stopwatch.html")
