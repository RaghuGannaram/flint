"""
    review/views.py
"""

from datetime import timedelta
from django.utils.timezone import now
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from review.forms import CreateReview  # pylint: disable=import-error
from .models import Review

User = get_user_model()


def review_catalog_view(request):
    """review_catalog_view function"""
    reviews = Review.objects.all()

    if request.method == "GET":
        query = request.GET.get("q", "").strip()
        min_rating = request.GET.get("min_rating", "").strip()
        recent_days = request.GET.get("recent_days", "").strip()

        min_rating = int(min_rating) if min_rating.isdigit() else None
        recent_days = int(recent_days) if recent_days.isdigit() else None

        if query:
            reviews = search_reviews(query, min_rating, recent_days)

    return render(request, "review/catalog.html", {"reviews": reviews})


def review_information_view(request, slug):
    """review_information_view function"""
    review = Review.objects.get(slug=slug)
    review_rating = range(review.rating)
    total_rating = range(5 - review.rating)
    return render(
        request,
        "review/information.html",
        {
            "review": review,
            "review_tags": review.tags,
            "review_rating": review_rating,
            "total_rating": total_rating,
        },
    )


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


def search_reviews(query, min_rating=None, recent_days=None):
    """search_reviews function"""
    print("Searching...", query, min_rating, recent_days)

    reviews = Review.objects.annotate(
        search=SearchVector("product_name", "content"),
        rank=SearchRank(SearchVector("product_name", "content"), SearchQuery(query)),
        similarity=TrigramSimilarity("product_name", query),
        distance=TrigramDistance("product_name", query),
    )

    reviews = reviews.filter(
        Q(search=SearchQuery(query))
        | Q(similarity__gt=0.2)
        | Q(distance__lt=0.8)
        | Q(tags__icontains=query)
    )
    if min_rating:
        reviews = reviews.filter(rating__gte=min_rating)

    if recent_days:
        reviews = reviews.filter(created_at__gte=now() - timedelta(days=recent_days))

    return reviews.order_by("-rank", "-similarity", "distance")
