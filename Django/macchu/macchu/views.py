from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = 'home.html'
    
class RankView(View):
    def get(self, request):
        from .beer_repository import BeerRepository
        import json

        beer_rank = BeerRepository()
        user_click_count = beer_rank.user_click_rank()
        recommend_count = beer_rank.recommend_rank()

        rank_list = [user_click_count, recommend_count]
        json_beer = json.dumps(rank_list, ensure_ascii=False)

        return HttpResponse(json_beer, content_type="application/json")