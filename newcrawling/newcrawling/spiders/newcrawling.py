from urllib.request import urlopen
import scrapy
from newcrawling.items import NewcrawlingItem

class NewcrawlingCrawlerSpider(scrapy.Spider):

    name = "newcrawling"

    def start_requests(self):
        headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        for i in range(1,3):
            url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EA%B8%88%EB%A6%AC&sort=0&photo=0&field=0&pd=3&ds=2011.01.01&de=2022.11.21&cluster_rank=24&mynews=1&office_type=1&office_section_code=8&news_office_checked=2227&nso=so:r,p:from20110101to20221121,a:all&start={0}'.format(i)
            yield scrapy.Request(url=url,
                                    callback=self.parse, headers=headers)

#    def parse(self, response):
#        for i in range(2,46):
#            for sel in response.xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tbody/tr[i]'):
#                item = ReportItem()

#                item['title'] = sel.xpath('/td[1]/a/text()').extract()[0]
#                item['date'] = sel.xpath('/td[4]/text()').extract()
#                item['pdf_url'] = sel.xpath('td[3]/a/@href').extract()

#            yield item
 

# //*[@id="sp_nws159"]/div/div/a # 기사제목
# //*[@id="sp_nws159"]/div/div/div[1]/div[2]/a # 언론사
# //*[@id="sp_nws174"]/div/div/div[1]/div[2]/span # Date

    def parse(self, response):
        item = NewcrawlingItem()
        for i in range(1, 30):
            if not response.xpath('//*[@id="sp_nws{0}"]/div/div/a'.format(i)).extract():
                continue

            else:
                # item['title'] = response.xpath('//*[@id="sp_nws{0}"]/div/div/a/text()'.format(i)).extract()
                # item['title_url'] =  response.xpath('//*[@id="sp_nws{0}"]/div/div/a/@href'.format(i)).extract()
                # item['press'] = response.xpath('//*[@id="sp_nws{0}"]/div/div/div[1]/div[2]/a/@href'.format(i)).extract()
                # item['date'] = response.xpath('//*[@id="sp_nws{0}"]/div/div/div[1]/div[2]/span/text()'.format(i)).extract()

                item['title'] = response.xpath('//*[@id="sp_nws{0}"]/div/div/a/text()'.format(i)).extract()
                item['title_url'] =  response.xpath('//*[@id="sp_nws{0}"]/div/div/a/@href'.format(i)).extract()
                # item['press'] = response.xpath('//*[@id="sp_nws{0}"]/div/div/div[1]/div[2]/a/@href'.format(i)).extract()
                item['date'] = response.xpath('//*[@id="sp_nws{0}"]/div/div/div[1]/div[2]/span/text()'.format(i)).extract()

                # add_url = item['pdf_url'][0]
                # with open('./pdf/{}.pdf'.format(item['title']), mode='wb') as f:
                #     f.write(urlopen(add_url).read())

                yield item

    # def file_download_from_web(url: str, file_name: str, file_extension: str):
    #     download = urlopen(url).read()
    #     file = './files/' + file_name + '.' + file_extension
