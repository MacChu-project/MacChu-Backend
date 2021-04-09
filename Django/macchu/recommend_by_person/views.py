from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = 'recommend_by_person/home.html'