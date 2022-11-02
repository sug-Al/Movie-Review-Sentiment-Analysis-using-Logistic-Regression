from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('dashboard/review/', views.review),
    path('dashboard/delete/<int:movie_review_id>/', views.delete_review),
    path('dashboard/edit/<int:movie_review_id>/', views.edit_review),
    path('edit/<int:movie_review_id>/', views.edit),
]