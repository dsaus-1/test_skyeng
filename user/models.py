from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
