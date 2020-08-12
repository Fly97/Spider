# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: request1
# @Create time: 2020/8/12 22:33
import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com'
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)
    with open('./html_list/sougou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据成功！')
