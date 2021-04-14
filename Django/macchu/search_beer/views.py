from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse


# Create your views here.

class HomeView(TemplateView):
    template_name = 'search_beer/search_page.html'

class SearchView(View):
    def get(self, request):

        beer_type = request.GET['type']
        beer_name = request.GET['name']

        from .search_beer import search_beer
        import json

        search_beers = search_beer()
        searched_beer = search_beers.search([beer_type, beer_name])
        json_beer = json.dumps(searched_beer, ensure_ascii=False)
        return HttpResponse(json_beer, content_type="application/json") 

