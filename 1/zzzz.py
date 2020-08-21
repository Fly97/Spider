# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: my_re
# @Create time: 2020/8/14 11:12
import re
import requests

if __name__ == '__main__':
    headers = {
        'Cookie': 'bid=h02Je0uMS88',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    
    url = 'https://www.douban.com/j/search_photo?q=王祖贤&limit=20&start=0'
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    print(page_text)