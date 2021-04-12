from django.contrib import admin
from django.urls import path, include

from .views import HomeView, SelectView

urlpatterns = [
    path('', HomeView.as_view(), name="recommend"),

    path('select/<str:key>', SelectView.as_view(), name="select")
]
