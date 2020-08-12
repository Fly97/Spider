# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: request_cbdb
# @Create time: 2020/8/13 0:54
import requests

if __name__ == '__main__':
    url='https://cbdb.fas.harvard.edu/cbdbapi/person.php?%20name=王昌'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    # data = {
    #     'on': 'true',
    #     'page': '1',
    #     'pageSize': '15',
    #     'productName': '',
    #     'conditionType': '1',
    #     'applyname': '',
    #     'applysn': ''
    # }
    # response = requests.get(url=url)
    # page_data = response.text
    # with open('cbdb.html','w',encoding='utf-8') as fw:
    #     fw.write(page_data)

    get_url='https://cbdb.fas.harvard.edu/cbdbapi/person.php?%20name=王昌'
    params={
        'name':'王昌'
    }
    response = requests.get(url=get_url,params=params,headers=headers)
    page_text = response.content.decode('utf-8')
    with open('cbdb2.html','w',encoding='utf-8') as fw:
        fw.write(page_text)
    print('finished!!')