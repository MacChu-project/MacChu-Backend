class BeerRepository:

    def __init__(self):
        self.connection_info = { 'host': 'macchu-db.cmq0yxrruhsw.ap-northeast-2.rds.amazonaws.com', 'db': 'MacChu', 'user': 'admin', 'password': 'a123456789', 'charset': 'utf8' }

    def select_beer(self, beer_idx):

        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select beer_idx, sweet, sour, tender, bitter, abundant from beer_taste where beer_idx = %s"
        cursor.execute(sql, (int(beer_idx),))

        rows = cursor.fetchall() # 반환 값은 tuple의 list [ (...), (...), ..., (...) ]
        keys = ["beer_idx", "sweet", "sour", "tender", "bitter", "abundant"]
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)

        conn.close()

        return result

    def recommended_beer(self, beer_idx):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select name, country, type, ABV, description, image from beer where beer_idx = %s"
        cursor.execute(sql, (int(beer_idx),))

        row = cursor.fetchone() # 반환 값은 tuple (...)
        keys = ["name", "country", "type", "ABV", "description", "image"]
        
        result = { key:value for key, value in zip(keys, row) }
            
        conn.close()

        return result

    def recommended_beer_info(self, beer_idx):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select beer_idx, name_ko, country, ABV, description from beer where beer_idx = %s"
        cursor.execute(sql, (int(beer_idx),))

        row = cursor.fetchone() # 반환 값은 tuple (...)
        keys = ["beer_idx", "name_ko", "country", "ABV","description"]
        
        result = dict(zip(keys, row))
            
        conn.close()

        return result
    
    def popular_beer_ranking_info(self):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql_for_index = "select beer_idx from pop_beer order by count limit 10"
        cursor.execute(sql)

        pop_beer_index = cursor.fetchone() # 반환 값은 tuple (...)

        sql_for_pop = "select beer_idx, name_ko, country, ABV, description from beer where beer_idx = %s"
        cursor.execute(sql, (int(pop_beer_index),))


        row = cursor.fetchone()
        keys = ["beer_idx", "name_ko", "country", "ABV", "description"]
        
        result = dict(zip(keys, row))
            
        conn.close()

        return result

    def user_click_count(self, beers_click):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        beers = list(map(int, beers_click.split(',')))

        sql = "UPDATE beer_rank SET user_click_count = user_click_count + 1 WHERE beer_idx = %s"

        for beer in beers:
            cursor.execute(sql, (int(beer)))

        conn.commit()
            
        conn.close()

    def recommend_count(self, beers_recommend):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "UPDATE beer_rank SET recommend_count = recommend_count + 1 WHERE beer_idx = %s"

        for beer in beers_recommend:
            cursor.execute(sql, (int(beer)))

        conn.commit()
            
        conn.close()