import scrapy
import time
import csv
 
class NewsUrlSpider(scrapy.Spider):
    name = "interest"
 
    def start_requests(self):
        headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        urls = 'https://finance.naver.com/research/debenture_list.naver?&page=1'

    
        for url in urls:
            yield scrapy.Request(url=url, headers=headers)
 
    def parse(self, response):
        print(response.text)
        news_lists = response.css('list_news > bx')
        for news_list in news_lists:
            print(news_list)
            title = news_list.css('a::text').extract()
            print('title: ',title)

