from django.contrib import admin
from django.urls import path, include

from .views import HomeView, SearchView

urlpatterns = [
    path('', HomeView.as_view(), name="search_beer"),
    path('result',SearchView.as_view(), name='search_result'),
]
