"""
    user/views.py
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


def register_view(request):
    """register_view function"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {"form": form})


def login_view(request):
    """login_view function"""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))

            return redirect("/")
    else:
        form = AuthenticationForm()
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
