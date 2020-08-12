# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: request_百度翻译
# @Create time: 2020/8/12 23:05
import requests

if __name__ == '__main__':
    # UA伪装:将User-Agent封装到字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    post_url = 'https://fanyi.baidu.com/sug'
    kw=input('inpur a word:')
    data = {
        'kw': kw
    }
    response = requests.post(url=post_url, data=data, headers=headers)
    page_json = response.json()
    print(page_json)
    print('translate:',page_json['data'][0]['v'])
