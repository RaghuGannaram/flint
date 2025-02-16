""" 
    user/models.py
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User class that extends the AbstractUser class."""

    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png")
    is_verified = models.BooleanField(default=False)
