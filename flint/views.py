"""
    flint/views.py
"""

from django.shortcuts import render


def home_view(request):
    """home_view funtion"""
    return render(request, "home.html")
