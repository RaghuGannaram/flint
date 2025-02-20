"""
    review/forms.py
"""

from django import forms
from review.models import Review


class CreateReview(forms.ModelForm):
    """CreateReview class"""

    class Meta:
        """Meta class"""

        model = Review
        fields = ["product_name", "category", "content", "tags", "rating", "image"]
