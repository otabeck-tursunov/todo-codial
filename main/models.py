from django.db import models

from user.models import User


class Reja(models.Model):
    sarlavha = models.CharField(max_length=255)
    batafsil = models.TextField(blank=True, null=True)
    bajarildi = models.BooleanField(default=False)
    muddat = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
