# -*- coding: utf-8 -*-
import scrapy
from fistBlood.items import FistbloodItem


class FirstSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # 数据解析
    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     all_data = []
    #     for div in div_list:
    #         author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         content = div.xpath('./a/div/span[1]/text()').extract()
    #         content = ''.join(content)
    #         # print(author, content)
    #         dic = {
    #             'author': str(author).replace('\n', '').replace('\r', '').replace(' ', ''),
    #             'content': content.replace('\n', '').replace('\r', '').replace(' ', '')
    #         }
    #         print(dic)
    #         all_data.append(dic)
    #     # print(all_data)
    #     return all_data

    def parse(self, response):
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        all_data = []
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a/div/span[1]/text()').extract()
            content = ''.join(content)
            # print(author, content)
            dic = {
                'author': str(author).replace('\n', '').replace('\r', '').replace(' ', ''),
                'content': content.replace('\n', '').replace('\r', '').replace(' ', '')
            }
            author = dic['author']
            content = dic['content']
            item = FistbloodItem()
            item['author'] = author
            item['content'] = content
            yield item
