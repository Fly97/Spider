import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['https://www.zhipin.com/job_detail/?query=python']
    # start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position=']
    start_urls = ['https://www.baidu.com']
    def parse(self, response):
        # print(response.text)
        li_list = response.xpath('//*[@id="s-top-left"]/a[1]/text()').extract()
        print(li_list)
        # for li in li_list:
        #     name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/text()').extract()
        #     abstract_src = 'https://www.zhipin.com' + li.xpath('./div/div[1]/div[1]/div/@href').extract()
        #     print(name, abstract_src)

