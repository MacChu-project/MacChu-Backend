import numpy as np
import pandas as pd

class beer_recommendation:
    
    def find_sim_beer(self, df, sim, beers):
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
                    if limit_add_beer == 3:
                        break

        # 입력한 세 개의 상품에 의해 추출된 9개의 상품 index를 리스트 형식으로 return
        return sim_beers
    

