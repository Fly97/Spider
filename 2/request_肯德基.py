# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: request_肯德基
# @Create time: 2020/8/12 23:56
import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10'
    }
    response = requests.post(url=url, data=data, headers=headers)
    page_data = response.text
    print(page_data)
    print('爬取完成！！')
