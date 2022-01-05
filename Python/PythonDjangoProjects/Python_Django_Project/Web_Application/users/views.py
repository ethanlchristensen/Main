from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from points.models import points_to_user
from users.models import *
from points.models import points_to_user

def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            f = form.save()
            p = points_to_user(points=0, user=f.username)
            p.save()
            messages.success(request, f'Your account has been created. Please login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def update_pass(request):
    form = request.POST
    print(form)

    

@login_required
def profile(request):
        context = {
            'points': points_to_user.objects.all()
        }
        return render(request, 'users/profile.html', context)