from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, null=False)
    adress = models.CharField(max_length=254, null=True)
    city = models.CharField(max_length=254, null=True)
    postal_code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.username, self.email


class Temperature(models.Model):
    temperature = models.FloatField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    idUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
