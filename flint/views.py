"""
    flint/views.py
"""

from django.shortcuts import render


def home_view(request):
    """home_view funtion"""
    return render(request, "home.html")

def about_view(request):
    """about_view funtion"""
    return render(request, "about.html")

def contact_view(request):
    """contact_view funtion"""
    return render(request, "contact.html")

def terms_view(request):
    """terms_view funtion"""
    return render(request, "terms.html")

def privacy_view(request):
    """privacy_view funtion"""
    return render(request, "privacy.html")
