import scrapy
import re
from datetime import datetime
import pandas as pd
from article_crawling.items import ArticleCrawlingItem
 
class ArticleSpider(scrapy.Spider):
    name = 'article'
    # allowed_domains = ['naver.com']
    url_format = "https://search.naver.com/search.naver?&where=news&query={0}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={1}&de={1}&docid=&nso=so:r,p:from{2}to{2},a:all&mynews=0&cluster_rank=41&start=1&refresh_start=0"
                # https://search.naver.com/search.naver?where=news&query={0}&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2021.04.21&de=2021.04.21&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom20210421to20210421
 
    def __init__(
        self, keyword="", start="", end="", **kwargs
    ):
        startdate =  datetime.strptime(start, "%Y-%m-%d")
        enddate =  datetime.strptime(end, "%Y-%m-%d")
 
        self.start_urls= []
        for cur_date in pd.date_range(startdate, enddate):
            self.start_urls.append(self.url_format.format(keyword, cur_date.strftime("%Y.%m.%d"), cur_date.strftime("%Y%m%d")))
 
    def parse(self, response):
        for item in response.css("ul.type01 li") :
            if item.css("a._sp_each_url") :
                url = item.css("a._sp_each_url::attr(href)").get()
                yield scrapy.Request(url, callback=self.parse_detail)
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    
    def parse_detail(self, response):   
        item = ArticleCrawlingItem()
        item['url']=response.url
        item['title']=response.css("h3#articleTitle::text").get()
        item['text']=''.join(response.css("div#articleBodyContents::text").getall()).replace("\n","").strip()
        item['date']=response.css("div.sponsor span.t11::text").get()
        item['logo']=response.css("div.press_logo img::attr(title)").get()
        
        
        yield item
