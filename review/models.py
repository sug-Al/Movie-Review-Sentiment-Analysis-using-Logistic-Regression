from django.db import models

class MovieReviews(models.Model):
    username = models.CharField(max_length=20, default="Anon")
    review = models.TextField(default="No review")
    sentiment = models.CharField(max_length=20, default="None")
    score = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
