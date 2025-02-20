"""
    user/forms.py
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()  # Reference the custom user model

class CustomUserCreationForm(UserCreationForm):
    """Custom form for user registration using the custom user model"""

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomAuthenticationForm(AuthenticationForm):
    """Custom authentication form to support custom user model"""

    class Meta:
        model = User
        fields = ["username", "password"]
