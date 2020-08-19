import scrapy


class XiaohSpider(scrapy.Spider):
    name = 'xiaoh'
    # allowed_domains = ['www']
    start_urls = ['http://www.521609.com/meinvxiaohua/']
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_nue = 2

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a[1]/img/@alt').extract_first()
            print(img_name)
    
        if self.page_nue <= 11:
            new_url = format(self.url % self.page_nue)
            self.page_nue += 1
            yield scrapy.Request(url=new_url, callback=self.parse)
