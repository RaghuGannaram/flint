"""
    review/models.py
"""

import os
import uuid
from django.utils.text import slugify
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex, BTreeIndex
from flint.storage_backends import S3MediaStorage
from user.models import User


def unique_review_path(_instance, filename):
    """Generate a unique file path for review images"""
    ext = os.path.splitext(filename)[-1]
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    return f"reviews/{unique_filename}"


class Review(models.Model):
    """Review model"""

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=255, db_index=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    tags = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    image = models.ImageField(
        storage=S3MediaStorage(), upload_to=unique_review_path, blank=True, null=True
    )
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class"""

        indexes = [
            GinIndex(
                fields=["product_name"],
                name="review_product_name_trgm_idx",
                opclasses=["gin_trgm_ops"],
            ),
            GinIndex(
                fields=["product_name", "content"],
                name="review_full_text_search_idx",
            ),
            GinIndex(
                fields=["tags"],
                name="review_tags_gin_idx",
            ),
            BTreeIndex(
                fields=["created_at"],
                name="review_created_at_idx",
            ),
        ]

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"{self.product_name}-{self.user if self.user else 'anonymous'}"
            )
        if isinstance(self.tags, str):
            self.tags = [tag.strip() for tag in self.tags.split(",") if tag.strip()]
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.product_name} - {self.user}"
            if self.user
            else f"{self.product_name} - Anonymous"
        )
