# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: 58ershoufang
# @Create time: 2020/8/13 23:03
import os

from lxml import etree
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'http://pic.netbian.com/4kmeinv/'
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    page_text = response.text
    # encode('iso-8859-1').decode('gbk') 解决中文乱码神器
    page_text = page_text.encode('iso-8859-1').decode('gbk')
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./picture'):
        os.mkdir('./picture')
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = './picture/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, 'download finish!!')
    # print(li_list)
    # print(len(li_list))
