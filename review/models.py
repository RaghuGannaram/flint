"""
    review/models.py
"""

from django.utils.text import slugify
from django.db import models
from user.models import User
from product.models import Product


class Review(models.Model):
    """Review class"""

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    images = models.ImageField(upload_to="reviews/", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.product.name}-{str(self.title)[:30]}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.title}"
