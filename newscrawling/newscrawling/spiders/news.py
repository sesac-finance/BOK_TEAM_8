import scrapy
import time
import csv
from newscrawling.items import NewscrawlingItem
 
class NewsUrlSpider(scrapy.Spider):
    name = "newsUrlCrawler"
 
    def start_requests(self):
        urls = 'https://finance.naver.com/research/debenture_list.naver?&page=1'
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        news_lists = response.css('tbody > file')
        for news_list in news_lists:
            print(news_list)
            title = news_list.css('a["href"]')
            print('title: ',title)