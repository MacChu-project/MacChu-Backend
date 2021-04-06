from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse

# class HomeView(TemplateView):
#     template_name = 'home.html'

def home(request):
    return render(request, 'recommend_by_person/home.html')

class SearchView(View):
    def get(self, request):

        from .dummy_repository import DummyRepository
        import json

        repository = DummyRepository()
        searched_dummy = repository.select_dummy_data()

        json_dummy = json.dumps(searched_dummy, ensure_ascii=False)
        return HttpResponse(json_dummy, content_type="application/json")

class SearchOneView(View):
    def get(self, request, key):

        from .dummy_repository import DummyRepository
        import json

        repository = DummyRepository()
        searched_dummy = repository.select_dummy_data_one(key)

        json_dummy = json.dumps(searched_dummy, ensure_ascii=False)
        return HttpResponse(json_dummy, content_type="application/json")