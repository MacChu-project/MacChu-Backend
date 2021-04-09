from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = 'recommend_by_person/home.html'

class SelectView(View):
    def get(self, request, key):
        from .beer_recommendation import recommendation_system
        import json

        beer_recommended = recommendation_system()
        searched_beers = beer_recommended.information_for_recommendation(key)
        json_beer = json.dumps(searched_beers, ensure_ascii=False)
        return HttpResponse(json_beer, content_type="application/json")