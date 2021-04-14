class search_beer:
    def __init__(self):
        self.connection_info = { 'host': 'macchu-db.cmq0yxrruhsw.ap-northeast-2.rds.amazonaws.com', 'db': 'MacChu', 'user': 'admin', 'password': 'a123456789', 'charset': 'utf8' }

    def search(self, beer):
        
        import pymysql
        
        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select beer_idx, name_ko, country, type, ABV, description from beer where " + beer[0] + " like \"%" + beer[1] + "%\""
        cursor.execute(sql)
        row = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["beer_idx","name_ko", "country", "type", "ABV", "description"]
        
        result = []

        for row_idx in row:
            result.append(dict(zip(keys, row_idx)))
    
            
        conn.close()

        return result

    
    