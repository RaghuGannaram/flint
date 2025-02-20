"""
    user/urls.py
"""

from django.urls import path
from user.views import register_view, login_view, profile_view, logout_view, edit_profile_view

app_name = "user"  # pylint: disable=invalid-name


urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
    path("logout/", logout_view, name="logout"),
    path("profile/edit/", edit_profile_view, name="edit_profile"),
]
