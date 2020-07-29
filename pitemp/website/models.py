from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from django.db.models.signals import post_save   # needed for token user 1/3
from django.dispatch import receiver     # needed for token user 2/3
from rest_framework.authtoken.models import Token    # needed for token user 3/3


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True, null=False)
    adress = models.CharField(max_length=254, null=True)
    city = models.CharField(max_length=254, null=True)
    postal_code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.username, self.email


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Temperature(models.Model):
    temperature = models.FloatField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    idUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.temperature, self.date
