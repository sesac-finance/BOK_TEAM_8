from urllib.request import urlopen
import scrapy
from report.items import ReportItem

class ReportCrawlerSpider(scrapy.Spider):

    name = "report"

    def start_requests(self):
        for i in range(1, 108):
            yield scrapy.Request("https://finance.naver.com/research/debenture_list.naver?keyword=&brokerCode=&searchType=writeDate&writeFromDate=2011-01-01&writeToDate=2021-12-31&page={0}".format(i),
                                    self.parse)


#    def parse(self, response):
#        for i in range(2,46):
#            for sel in response.xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tbody/tr[i]'):
#                item = ReportItem()

#                item['title'] = sel.xpath('/td[1]/a/text()').extract()[0]
#                item['date'] = sel.xpath('/td[4]/text()').extract()
#                item['pdf_url'] = sel.xpath('td[3]/a/@href').extract()

#            yield item
 



    def parse(self, response):
        item = ReportItem()
        for i in range(2,48):
            if not response.xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tr[{0}]/td[3]/a/@href'.format(i)).extract():
                continue

            else:
                item['title'] = response.xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tr[{0}]/td[1]/a/text()'.format(i)).extract()
                item['date'] = response.xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tr[{0}]/td[4]/text()'.format(i)).extract()
                item['pdf_url'] = response.xpath('//*[@id="contentarea_left"]/div[3]/table[1]/tr[{0}]/td[3]/a/@href'.format(i)).extract()

                add_url = item['pdf_url'][0]
                with open('./pdf/{}.pdf'.format(item['title']), mode='wb') as f:
                    f.write(urlopen(add_url).read())


                yield item

    # def file_download_from_web(url: str, file_name: str, file_extension: str):
    #     download = urlopen(url).read()
    #     file = './files/' + file_name + '.' + file_extension
