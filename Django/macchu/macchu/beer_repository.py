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

    def recommended_beer(self, symbol):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select name, country, type, ABV, description, image from beer where beer_idx = %s "
        cursor.execute(sql, (int(beer_idx),))

        row = cursor.fetchone() # 반환 값은 tuple (...)
        keys = ["name", "country", "type", "ABV", "description", "image"]
        
        result = { key:value for key, value in zip(keys, row) }
            
        conn.close()

        return result

    def user_click_rank(self):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select beer_idx, user_click_count from beer_rank Order by user_click_count desc Limit 12"
        cursor.execute(sql)

        rows = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["beer_idx", "user_click_count"]
        
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)
            
        conn.close()

        return result

    def recommend_rank(self):
        import pymysql

        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select beer_idx, recommend_count from beer_rank Order by recommend_count desc Limit 12"
        cursor.execute(sql)

        rows = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["beer_idx", "recommend_count"]
        
        #result = { key:value for key, value in zip(keys, row) }
        result = []
        for row in rows:
            row_dict = { key:value for key, value in zip(keys, row) }
            result.append(row_dict)
            
        conn.close()

        return result