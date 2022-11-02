from django.shortcuts import render, redirect
from .models import MovieReviews

from tfidf_logreg_module import tfidf_log_reg as tlr


def dashboard(request):
    movie_review = MovieReviews.objects.all()
    reviews = MovieReviews.objects.all().count()
    pos = MovieReviews.objects.filter(sentiment='Positive sentiment').count()
    neg = MovieReviews.objects.filter(sentiment='Negative sentiment').count()
    count = {
        'reviews': reviews,
        'pos': pos,
        'neg': neg
    }
    return render(request, "review.html", {"data": movie_review, "count": count})


def review(request):
    movie_review = MovieReviews()

    if request.method == "POST":
        movie_review.username = request.POST['username']
        movie_review.review = request.POST['review']
        text = [movie_review.review]
        movie_review.sentiment, movie_review.score = tlr.log_model(text)

    movie_review.save()
    return redirect(dashboard)


def delete_review(request, movie_review_id):
    movie_review = MovieReviews.objects.get(id=movie_review_id)
    movie_review.delete()
    return redirect(dashboard)


def edit_review(request, movie_review_id):
    movie_review = MovieReviews.objects.get(id=movie_review_id)
    return render(request, "edit.html", {"data": movie_review})


def edit(request, movie_review_id):
    movie_review = MovieReviews.objects.get(id=movie_review_id)
    if request.method == "POST":
        movie_review.username = request.POST['username']
        movie_review.review = request.POST['review']
        text = [movie_review.review]
        movie_review.sentiment, movie_review.score = tlr.log_model(text)

    movie_review.save()
    return redirect(dashboard)




