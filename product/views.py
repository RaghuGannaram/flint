"""
    product/views.py
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from .models import Product
from .forms import CreateProduct  # pylint: disable=import-error

User = get_user_model()

def product_catalog_view(request):
    """product_catalog_view function"""
    products = Product.objects.all()
    return render(request, "product/catalog.html", {"products": products})


def product_information_view(request, slug):
    """product_information_view function"""
    product = Product.objects.get(slug=slug)
    return render(request, "product/information.html", {"product": product})


@login_required(login_url="user:login")
def product_enroll_view(request):
    """product_enroll_view function"""
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            newproduct = form.save(commit=False)

            newproduct.user = User.objects.get(pk=request.user.pk)

            newproduct.save()
            return redirect("product:catalog")
    else:
        form = CreateProduct()
    return render(request, "product/enroll.html", {"form": form})
