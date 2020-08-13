# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: xpath
# @Create time: 2020/8/13 22:39
from lxml import etree

if __name__ == '__main__':
    tree = etree.parse('test.html')
    # r = tree.xpath('//div[@class="tang"]//li//text()')[0]
    r = tree.xpath('//div[@class="tang"]//li/a/@href')
    print(r)
    print(len(r))
