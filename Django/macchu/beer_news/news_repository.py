class SearchNews:
    def __init__(self):
        self.connection_info = { 'host': 'macchu-db.cmq0yxrruhsw.ap-northeast-2.rds.amazonaws.com', 'db': 'MacChu', 'user': 'admin', 'password': 'a123456789', 'charset': 'utf8' }


    def before_search(self):
        
        import pymysql
        
        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select DATE_FORMAT(news_date, \'%Y-%m-%d\'), news_title, news_content, news_url from beer_news order by news_date desc"
        cursor.execute(sql)
        row = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["news_date","news_title", "news_content", "news_url"]
        
        result = []

        for row_idx in row:
            result.append(dict(zip(keys, row_idx)))
    
            
        conn.close()
        
        return result

    def after_search(self, news):
        
        import pymysql
        
        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select DATE_FORMAT(news_date, \'%Y-%m-%d\'), news_title, news_content, news_url from beer_news where news_title like \"%" + news + "%\" order by news_date desc limit 10"
        cursor.execute(sql)
        row = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["news_date","news_title", "news_content", "news_url"]
        
        result = []

        for row_idx in row:
            result.append(dict(zip(keys, row_idx)))
    
            
        conn.close()

        return result

    def news_count_result(self):
        
        import pymysql
        
        conn = pymysql.connect(**self.connection_info)
        cursor = conn.cursor()

        sql = "select DATE_FORMAT(news_date, \'%Y-%m-%d\'), news_title, news_content, news_url from beer_news order by news_view_count desc limit 10"
        cursor.execute(sql)
        row = cursor.fetchall() # 반환 값은 tuple (...)
        keys = ["news_date","news_title", "news_content", "news_url"]
        
        result = []

        for row_idx in row:
            result.append(dict(zip(keys, row_idx)))
    
            
        conn.close()

        return result

