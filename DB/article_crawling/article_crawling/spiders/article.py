import scrapy
import re
from datetime import datetime
import pandas as pd
from article_crawling.items import ArticleCrawlingItem
 
class ArticleSpider(scrapy.Spider):
    name = 'article'
    # allowed_domains = ['naver.com']
    url_format = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query={0}&sort=0&photo=0&field=0&pd=3&ds={1}&de={1}&cluster_rank=28&office_section_code=0&news_office_checked=&nso=so:r,p:from{2}to{2},a:all&start=1"
                 
    def __init__(
        self, keyword="", start="", end="", **kwargs
    ):
        startdate =  datetime.strptime(start, "%Y-%m-%d")
        enddate =  datetime.strptime(end, "%Y-%m-%d")
 
        self.start_urls= []
        for cur_date in pd.date_range(startdate, enddate):
            self.start_urls.append(self.url_format.format(keyword, cur_date.strftime("%Y.%m.%d"), cur_date.strftime("%Y%m%d")))
 
    def parse(self, response):
        for item in response.css("ul.list_news li") :
            if item.css("a.info") :
                url_list = item.css("a.info::attr(href)").getall()
                if len(url_list) > 1:
                    url = url_list[1]
                    yield scrapy.Request(url, callback=self.parse_detail)
        
        next_page = response.css('a.btn_next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_detail(self, response):   
        item = ArticleCrawlingItem()
        item['news_url']=response.url
        item['news_title']=response.css("h3#articleTitle::text").get()
        item['news_content']=''.join(response.css("div#articleBodyContents::text").getall()).replace("\n","").strip()
        raw_date = response.css("div.sponsor span.t11::text").get()

        if raw_date[12:14] == '오후':
            date_data = raw_date[0:4] + '-' + raw_date[5:7] + '-' + raw_date[8:10] + ' ' + str(int(raw_date[-5:-3].split()[0])+12) + raw_date[-3:] + ':00'
        else:
            if len(raw_date[-5:-3].split()[0]) == 1:
                date_data = raw_date[0:4] + '-' + raw_date[5:7] + '-' + raw_date[8:10] + ' 0' + raw_date[-5:-3].split()[0] + raw_date[-3:] + ':00'
            else:
                date_data = raw_date[0:4] + '-' + raw_date[5:7] + '-' + raw_date[8:10] + ' ' + raw_date[-5:-3].split()[0] + raw_date[-3:] + ':00'

        item['news_date'] = date_data
        
        if item['news_title'] != None:
            yield item