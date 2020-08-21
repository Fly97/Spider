import scrapy


class Mp3Spider(scrapy.Spider):
    name = 'mp3'
    allowed_domains = ['http://tool.liumingye.cn/music/?page=audioPage']
    start_urls = ['http://http://tool.liumingye.cn/music/?page=audioPage/']

    def parse(self, response):
        ''
