import scrapy


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['airbnb.com.br']
    start_urls = ['http://airbnb.com.br/']

    def parse(self, response):
        pass
