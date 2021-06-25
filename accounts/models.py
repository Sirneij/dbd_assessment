from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField('First Name', max_length=255, blank=True,
                                  null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                 null=False)
    phone = models.CharField(max_length=20, blank=True, null=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to="users-thumbnails/%Y/%m/%d/", null=True)
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"
