from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.home, name='reservation-home'),
    path('about/', views.about, name='reservation-about'),
    path('make_reservation/', views.make_reservation, name='make-reservation'),
    path('addReservationItem/', views.add_reservation),
]
