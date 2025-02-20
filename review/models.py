"""
    review/models.py
"""

from django.utils.text import slugify
from django.db import models
from user.models import User


class Review(models.Model):
    """Review model"""

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    tags = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    image = models.ImageField(upload_to="reviews/", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.product_name}-{str(self.user)[:30]}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name} - {self.user}"
