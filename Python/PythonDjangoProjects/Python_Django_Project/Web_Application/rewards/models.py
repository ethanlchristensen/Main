from django.db import models

class Reward(models.Model):
    product = models.TextField()
    points = models.IntegerField()
    description = models.TextField()
    vendor = models.TextField()

    def __str__(self):
        return self.product