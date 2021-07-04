from django.db import models
from django.contrib.auth.models import User

class Coop(models.Model):
    url = models.CharField(max_length=100)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.url