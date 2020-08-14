# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: 正则解析
# @Create time: 2020/8/13 12:48
import requests
import os
import re

if __name__ == '__main__':
    if os.path.exists('./decument/qiutulibs'):
        os.mkdir('./document/qiutulibs')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://www.qiushibaike.com/imgrank/'
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    # 开始正则解析
    ex = '<div class="thumb">.*?<img src="(.*?)" alt=".*?</div>'
    img_list = re.findall(ex, page_text, re.S)
    for img in img_list:
        img_url = 'https:' + img
        img_data = requests.get(url=img_url, headers=headers).content
        img_name = str(img).split('/')[-1]
        img_path = './document/qiutulibs/' + str(img_name)
        with open(img_path, 'wb') as fw:
            fw.write(img_data)
        print(img_name, ' has been download success!!!')
        # print(img)
    print('一共爬取%d张照片！！' % (len(img_list)))
