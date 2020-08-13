# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: xpath_jianli
# @Create time: 2020/8/14 0:06
import os
from lxml import etree
import requests

if __name__ == '__main__':
    url = 'http://sc.chinaz.com/jianli/free.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    # page_text = page_text.encode('iso-8859-1').decode('gbk')
    tree = etree.HTML(page_text)
    jianli_list = tree.xpath('//*[@id="container"]/div')

    if not os.path.exists('./jianli'):
        os.mkdir('./jianli')
    for jianli in jianli_list:
        jianli_href = jianli.xpath('./a/@href')[0]
        jianli_name = jianli.xpath('./a/img/@alt')[0]
        jianli_text = requests.get(url=jianli_href, headers=headers).text
        tree1 = etree.HTML(jianli_text)
        jianli_src = tree1.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        jianli_data = requests.get(url=jianli_src, headers=headers).content
        jianli_path = 'jianli/' + jianli_name + '.rar'
        with open(jianli_path, 'wb') as fp:
            fp.write(jianli_data)
            print(jianli_name, ' download finished!!!')
    print('download finished!!')
