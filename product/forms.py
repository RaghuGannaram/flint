"""
    product/forms.py
"""

from django import forms
from product.models import Product


class CreateProduct(forms.ModelForm):
    """CreatePost class"""

    class Meta:
        """Meta class"""

        model = Product
        fields = ["name", "category", "slug", "image", "description"]
