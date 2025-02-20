"""
    review/views.py
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
from review.forms import CreateReview  # pylint: disable=import-error
from .models import Review

User = get_user_model()


def review_catalog_view(request):
    """review_catalog_view function"""
    reviews = Review.objects.all()
    return render(request, "review/catalog.html", {"reviews": reviews})


def review_information_view(request, slug):
    """review_information_view function"""
    review = Review.objects.get(slug=slug)
    return render(request, "review/information.html", {"review": review})


@login_required(login_url="user:login")
def review_enroll_view(request):
    """review_enroll_view function"""
    if request.method == "POST":
        form = CreateReview(request.POST, request.FILES)
        if form.is_valid():
            newreview = form.save(commit=False)

            newreview.user = User.objects.get(pk=request.user.pk)

            newreview.save()
            return redirect("review:catalog")
    else:
        form = CreateReview()
    return render(request, "review/enroll.html", {"form": form})
