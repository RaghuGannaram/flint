"""
    category/models.py
"""

from django.utils.text import slugify
from django.db import models


class Category(models.Model):
    """Category class"""

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
