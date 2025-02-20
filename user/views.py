"""
    user/views.py
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    UserProfileForm,
)  # Import custom forms


def register_view(request):
    """register_view function"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request, "user/register.html", {"form": form})


def login_view(request):
    """login_view function"""
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))

            return redirect("/")
    else:
        form = CustomAuthenticationForm()
    return render(request, "user/login.html", {"form": form})


@login_required(login_url="user:login")
def profile_view(request):
    """profile_view function"""
    user = request.user
    return render(request, "user/profile.html", {"user": user})


def logout_view(request):
    """logout_view function"""
    if request.method == "POST":
        logout(request)
        return redirect("/")


@login_required
def edit_profile_view(request):
    """Handles profile update form"""

    user = request.user  # Get current user

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("user:profile")  # Redirect to profile page after update
    else:
        form = UserProfileForm(instance=user)

    return render(request, "user/edit_profile.html", {"form": form})
