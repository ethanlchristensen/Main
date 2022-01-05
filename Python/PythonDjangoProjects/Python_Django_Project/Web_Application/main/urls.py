from django.urls import path

from . import views
from users import views as user_views
from points import views as points_views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('register/', user_views.register, name='register'),
    path('stopwatch/', views.stopwatch, name='main-stopwatch'),
]