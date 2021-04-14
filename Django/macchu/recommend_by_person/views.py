from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse

class HomeView(TemplateView):
    template_name = 'recommend_by_person/recommendation_page.html'

# class HomePopAndReRankingView(View):
#     def get(self, request):
#         from .beer_repository import BeerRepository
#         import json

#         beer_repository = BeerRepository()
#         pop_beer = beer_repository.popular_beer_ranking_info()
#         recommended_beer = beer_repository.recommended_beer_ranking_info()

#         beer_list = [pop_beer, recommended_beer]
#         json_list = json.dumps(beer_list, ensure_ascii=False)
#         return HttpResponse(json_list, content_type="application/json")

class SelectView(View):
    def get(self, request, key):
        from .beer_recommendation import recommendation_system
        from .beer_repository import BeerRepository
        import json

        beer_recommended = recommendation_system()

        beer_db = BeerRepository()
        # key를 가지고 mysql의 ranking 테이블에서 count를 1씩 증가시키는 소스코드(작성중)
        beer_db.user_click_count(key)

        searched_beers = beer_recommended.information_for_recommendation(key)
        # 가져온 search_beer에서 idx값만 뽑아서 ranking 테이블에 count를 1씩 증가시켜야 함.
        
        # 아래는  idx 가져오는 소스코드 
        
        # ranking 테이블에 count를 증가시키는 소스코드(작성중)
        
        json_beer = json.dumps(searched_beers, ensure_ascii=False)
        return HttpResponse(json_beer, content_type="application/json")