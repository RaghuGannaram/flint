"""
    review/urls.py
"""

from django.urls import path

from review.views import review_catalog_view, review_information_view, review_enroll_view

app_name = "review"  # pylint: disable=invalid-name

urlpatterns = [
    path("catalog/", review_catalog_view, name="catalog"),
    path("information/<slug:slug>/", review_information_view, name="information"),
    path("enroll/", review_enroll_view, name="enroll"),
]
