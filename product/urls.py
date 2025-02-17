"""
    product/urls.py
"""

from django.urls import path

from product.views import product_catalog_view, product_information_view, product_enroll_view

app_name = "product"  # pylint: disable=invalid-name

urlpatterns = [
    path("catalog/", product_catalog_view, name="catalog"),
    path("information/<slug:slug>/", product_information_view, name="information"),
    path("enroll/", product_enroll_view, name="enroll"),
]
