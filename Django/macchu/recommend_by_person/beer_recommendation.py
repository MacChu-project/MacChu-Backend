import numpy as np
import pandas as pd

class recommendation_system:

    def information_for_recommendation(self, key):
        '''
        사용자가 선택한 맥주들의 인덱스를 리스트로 저장하고 추천 시스템에 필요한 정보들을 불러오는 함수

        key : ,를 구분으로 user가 선택한 3개의 맥주들로 이루어진 list
        '''

        # 맥주 데이터를 DataFrame 형식으로 load
        from sqlalchemy import create_engine

        engine = create_engine('mysql://admin:a123456789@macchu-db.cmq0yxrruhsw.ap-northeast-2.rds.amazonaws.com/MacChu', convert_unicode=True)
        conn = engine.connect()

        beer_df = pd.read_sql_table('beer_taste', conn)

        # 특정 맥주의 index 입력(세 개)
        beers = list(map(int, key.split(',')))

        # Cosine Similarity load
        taste_sim = np.load('recommend_by_person/outputs/taste_sim.npy')

        recommended_beers = self.find_sim_beer(beer_df, taste_sim, beers)

        from .beer_repository import BeerRepository
        beer_db = BeerRepository()
        beer_db.recommend_count(recommended_beers)

        result = self.get_beer_info(recommended_beers)

        return result
    
    def find_sim_beer(self, df, sim, beers):
        '''
        user가 선택한 맥주들의 유사도를 계산해 맥주 하나당 3개씩의 추천 맥주를 뽑고 정렬해서 리스트로 반환하는 함수

        df : idx, name, sweet, sour, tender, bitter, abundant로 이루어진 csv 파일
        sim : 각 맥주들이 유사도로 이루어진 npy 파일
        beers : user가 선택한 3개의 맥주들로 이루어진 list
        '''

        # 유사도에 따라 추출한 맥주 index를 저장할 리스트 초기화
        sim_beers = []

        # for문을 사용하여 input 데이터로 들어온 세 개의 맥주를 순차적으로 분석
        for beer in beers:
            # 유사도에 따라 상위 10개의 index를 추출
            sim1 = sim[beer] 
            top = np.argsort(sim1)[::-1][:10]

            # 추출한 index에서 자신이 포함되어 있는지 확인
            index_one = np.where(top==beer)[0][0]
            top = np.delete(top, index_one)
            limit_add_beer = 0
            # 추출된 index 하나하나 추출하여 검사
            for sim_beer in top:
                # 추출된 index에서 사용자가 선택한 맥주가 포함되는지 확인
                if sim_beer in beers:
                    continue
                # 추출된 index에서 현재까지의 추천 시스템 리스트에 포함된 것이 있는지 확인
                elif sim_beer in sim_beers:
                    continue
                # 아닐 경우 추천 리스트에 포함시키고, 3개를 추천하면 다음 추출 or 끝내기
                else:
                    sim_beers.append(sim_beer)
                    limit_add_beer += 1
                    if len(beers) == 3 and limit_add_beer == 3:
                        break
                    elif len(beers) == 2 and limit_add_beer == 5:
                        break
                    if len(beers) == 1 and limit_add_beer == 9:
                        break
                    

        # 입력한 세 개의 상품에 의해 추출된 9개의 상품 index를 리스트 형식으로 return
        return sim_beers

    def get_beer_info(self, beer_idxes):
        from .beer_repository import BeerRepository

        beer_list = []
        beer_db = BeerRepository()
        
        for beer_idx in beer_idxes:
            beer_list.append(beer_db.recommended_beer_info(beer_idx))

        return beer_list