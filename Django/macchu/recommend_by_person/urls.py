from django.contrib import admin
from django.urls import path, include

from .views import SearchView, SearchOneView
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('search/', SearchView.as_view(), name="search"),
    path('search/<str:key>', SearchOneView.as_view(), name="search"),
]
