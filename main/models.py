from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class Deal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title