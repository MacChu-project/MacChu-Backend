from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse


# Create your views here.


class HomeView(TemplateView):
    template_name = 'beer_news/home.html'

class BeforeView(View):
    def get(self, request):

        from .news_repository import SearchNews
        import json

        before_news = SearchNews()
        before_news_list = before_news.before_search()
        count_news_list = before_news.news_count_result()
        json_news = json.dumps([before_news_list, count_news_list], ensure_ascii=False)
        return HttpResponse(json_news, content_type="application/json") 

class SearchView(View):
    def get(self, request):

        news_name = request.GET['name']

        from .news_repository import SearchNews
        import json

        search_news = SearchNews()
        search_news_list = search_news.after_search(news_name)
        json_news = json.dumps(search_news_list, ensure_ascii=False)
        return HttpResponse(json_news, content_type="application/json") 
