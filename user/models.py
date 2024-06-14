from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ism = models.CharField(max_length=255, blank=True, null=True)
    familiya = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
