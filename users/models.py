from django.db import models

# Create your models here.

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Avatar')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Country')
    email_verify = models.BooleanField(default=False, verbose_name='email_verify')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
