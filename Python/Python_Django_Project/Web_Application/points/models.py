from django.db import models
from django.db.models.fields import IntegerField, TextField

class points_to_user(models.Model):
    points = IntegerField()
    user = TextField()

    def __str__(self):
        return self.user
