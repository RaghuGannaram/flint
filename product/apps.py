"""
    product/apps.py
"""

from django.apps import AppConfig


class ProductConfig(AppConfig):
    """ProductConfig class"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "product"
