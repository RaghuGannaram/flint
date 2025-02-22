""" 
    user/models.py
"""

import os
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from flint.storage_backends import S3MediaStorage


def unique_avatar_path(_instance, filename):
    """Generate a unique file path for user avatars"""
    ext = os.path.splitext(filename)[-1]
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    return f"avatars/{unique_filename}"


class User(AbstractUser):
    """User class that extends the AbstractUser class."""

    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(
        storage=S3MediaStorage(), upload_to=unique_avatar_path, blank=True, null=True
    )
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
