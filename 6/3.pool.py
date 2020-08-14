# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: 3.pool
# @Create time: 2020/8/14 22:28
import os

import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}


def get_url_text(url):
    response = requests.get(url=url, headers=headers)
    return response.text


def get_url_content(url):
    response = requests.get(url=url, headers=headers)
    return response.content


def get_mp4_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载！！')
    mp4_path='./video/'+str(dic['name'])
    data = requests.get(url=url, headers=headers).content
    with open(mp4_path, 'wb') as fp:
        fp.write(data)
        print(dic['name'], '下载成功！！')


if __name__ == '__main__':
    url = 'https://www.pearvideo.com/category_5'
    # response.encoding = 'utf-8'
    page_text = get_url_text(url)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
    urls = []
    for li in li_list:
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        detail_page_text = get_url_text(detail_url)
        ex = 'srcUrl="(.*?)",vdoUrl'
        # print(detail_page_text)
        mp4_url = re.findall(ex, detail_page_text)[0]
        # print(mp4_url)
        dic = {
            'name': name,
            'url': mp4_url
        }
        urls.append(dic)
    if not os.path.exists('./video'):
        os.mkdir('./video')
    pool = Pool(4)
    pool.map(get_mp4_data, urls)
    pool.close()
    pool.join()
