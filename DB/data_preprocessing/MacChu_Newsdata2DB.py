import json
import pymysql
import pandas as pd

# Load Data
file = r"C:\\Users\\ehhah\\dev\\jupyterlab\\test.json"
data = pd.read_json(file, encoding="utf-8")

# DB
MC_DB = pymysql.connect(host='macchu-db.cmq0yxrruhsw.ap-northeast-2.rds.amazonaws.com',
                        port=3306,
                        user='admin',
                        passwd='a123456789',
                        db='MacChu',
                        charset='utf8')
cursor = MC_DB.cursor()


def insert(table, columns, values):
    sql_qr2 = """
        INSERT INTO {0}({1})
        VALUES ({2})
    """.format(table, columns, values)
    cursor.execute(sql_qr2)
    MC_DB.commit()


# Data Input
data_list = []  # 데이터 확인을 위한 리스트 선언
for i in range(len(data)):  # 데이터 수 만큼 반복

    data_list.append(
        {"news_date": data['date'][i],
         "news_title": data['title'][i],
         "news_content": data['text'][i],
         "news_url": data['url'][i]
         })

    try:
        insert('beer_news', 'news_date, news_title, news_content, news_url',
               '"{}", "{}", "{}", "{}"'.format(data['date'][i], data['title'][i], data['text'][i], data['url'][i]))
    except:
        print("error = " + '"{}", "{}", "{}", "{}"'.format(data['date'][i], data['title'][i], data['text'][i],
                                                           data['url'][i]))
        pass