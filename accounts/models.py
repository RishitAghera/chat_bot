from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES=PLATFORM=(
        ('male','Male'), ('female','Female')
    )
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    Address = models.TextField(max_length=150)

