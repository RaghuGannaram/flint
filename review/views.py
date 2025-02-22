"""
    review/views.py
"""

import logging
from datetime import timedelta
from django.utils.timezone import now
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from review.forms import CreateReview, ReviewEditForm  # pylint: disable=import-error
from .models import Review

User = get_user_model()
logger = logging.getLogger("django.request")


def review_catalog_view(request):
    """review_catalog_view function"""

    if request.method == "GET":
        query = request.GET.get("q", "").strip()
        min_rating = request.GET.get("min_rating", "").strip()
        recent_days = request.GET.get("recent_days", "").strip()

        page = request.GET.get("page", 1)
        per_page = 12

        min_rating = int(min_rating) if min_rating.isdigit() else None
        recent_days = int(recent_days) if recent_days.isdigit() else None

        if query or (min_rating is not None) or (recent_days is not None):
            reviews = search_reviews(query, min_rating, recent_days)
        else:
            reviews = Review.objects.all().order_by("-created_at")

        paginator = Paginator(reviews, per_page)

        try:
            reviews = paginator.page(page)
        except PageNotAnInteger:
            reviews = paginator.page(1)
        except EmptyPage:
            reviews = paginator.page(paginator.num_pages)

    return render(request, "review/catalog.html", {"reviews": reviews})


def review_information_view(request, slug):
    """review_information_view function"""

    review = get_object_or_404(Review, slug=slug)
    is_author = review.user == request.user
    review_rating = range(review.rating)
    total_rating = range(5 - review.rating)
    return render(
        request,
        "review/information.html",
        {
            "review": review,
            "is_author": is_author,
            "review_tags": review.tags,
            "review_rating": review_rating,
            "total_rating": total_rating,
        },
    )


@login_required(login_url="user:login")
def review_enroll_view(request):
    """review_enroll_view function"""
    if request.method == "POST":
        logger.info(
            "######################## user is enrolling a new review",
        )
        form = CreateReview(request.POST, request.FILES)
        if form.is_valid():
            newreview = form.save(commit=False)

            newreview.user = User.objects.get(pk=request.user.pk)

            newreview.save()
            return redirect("review:catalog")
    else:
        form = CreateReview()
    return render(request, "review/enroll.html", {"form": form})


@login_required(login_url="user:login")
def review_edit_view(request, slug):
    """review_edit_view function"""
    logger.info("Hello=====================>")
    review = get_object_or_404(Review, slug=slug)

    if review.user != request.user:
        return redirect("review:information", slug=review.slug)

    if request.method == "POST":
        form = ReviewEditForm(request.POST, instance=review)
        logger.info("######################## user is editing a new review ")
        if form.is_valid():
            form.save()
            return redirect("review:information", slug=review.slug)
    else:
        form = ReviewEditForm(instance=review)

    return render(request, "review/edit.html", {"form": form, "review": review})


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
