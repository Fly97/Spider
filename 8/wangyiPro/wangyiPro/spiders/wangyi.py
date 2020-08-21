import scrapy
from wangyiPro.items import WangyiproItem
from selenium import webdriver

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']

    li_url_list = []

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='D:\workspace\Spider\8\wangyiPro\wangyiPro\spiders\chromedriver.exe')

    def parse(self, response):
        wangyi_list = [6, 7]
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        for index in wangyi_list:
            li_url = li_list[index].xpath('./a/@href').extract_first()
            print(li_url)
            self.li_url_list.append(li_url)

            # 依次对每一个板块对应的页面进行请求
        for url in self.li_url_list:  # 对每一个板块的url进行请求发送
            yield scrapy.Request(url, callback=self.parse_model)


    def parse_model(self, response):
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/h3/a/text() | ./div/div[1]/h3/a/text()').extract_first()
            new_detial_url = div.xpath('./div/h3/a/@href | ./div/div[1]/h3/a/@href').extract_first()
            if title == None:
                continue
            print(title, new_detial_url)
            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url=new_detial_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        # p_list = response.xpath('//*[@id="endText"]/p')
        # content_list = []
        # for p in p_list:
        #     p_text = p.xpath('./text()').extract_first()
        #     content_list.append(p_text)
        # content = ''.join('%s' %id for id in content_list)
        # item = response.meta['item']
        # item['content'] = content
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self, spider):
        self.bro.quit()