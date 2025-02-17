"""
    product/models.py
"""

from django.utils.text import slugify
from django.db import models
from category.models import Category
from user.models import User


class Product(models.Model):
    """Product Model"""

    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
