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

    # Fix the related_name conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",
        blank=True,
    )

    def __str__(self):
        return str(self.username)
