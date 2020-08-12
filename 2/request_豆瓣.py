# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: douban_异步
# @Create time: 2020/8/12 23:26
import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '100'
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_json = response.json()
    print(json.dumps(page_json, sort_keys=False, indent=4, ensure_ascii=False))
    print('共爬取%d部电影！！' % (len(page_json)))
