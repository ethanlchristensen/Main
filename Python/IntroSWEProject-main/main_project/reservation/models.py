from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    reservationName = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    peopleCount = models.IntegerField()
    boothTable = models.TextField()
    requests = models.TextField()
    user = models.TextField()
    restaurant = models.TextField()

    def __str__(self):
        n = self.restaurant + ", " + self.reservationName
        return n

