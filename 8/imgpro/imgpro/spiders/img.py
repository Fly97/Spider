import scrapy
from imgpro.items import ImgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['ww']
    start_urls = ['http://sc.chinaz.com/tupian/']

    base_url = 'http://sc.chinaz.com/tupian/index_%d.html'
    page_num = 2

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            # 注意：使用伪属性
            src = div.xpath('./div/a/img/@src2').extract_first()
            name = div.xpath('./p/a/text()').extract()[0]
            name = str(''.join(name)).replace('图片', '') + '.jpg'
            item = ImgproItem()
            item['src'] = src
            item['name'] = name
            yield item
        if self.page_num <= 10:
            print('第%d页爬取成功！！！' % (self.page_num))
            new_url = format(self.base_url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)
