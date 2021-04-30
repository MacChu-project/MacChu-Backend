from django.contrib import admin
from django.urls import path, include

from .views import HomeView, BeforeView, SearchView

urlpatterns = [
    path('', HomeView.as_view(), name="beer_news"),
    path('before', BeforeView.as_view(), name="beer_news_before"),
    path('result', SearchView.as_view(), name="beer_news_search"),
]