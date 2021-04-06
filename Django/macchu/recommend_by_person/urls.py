from django.contrib import admin
from django.urls import path, include

# from .views import HomeView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
]
