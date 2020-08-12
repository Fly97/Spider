# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: request_服务平台
# @Create time: 2020/8/13 0:12
import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    response = requests.post(url=url, data=data, headers=headers)
    page_json = response.json()
    print(json.dumps(page_json, indent=4, ensure_ascii=False))
    id_list = []
    for dic in page_json['list']:
        id_list.append(dic['ID'])
    print('所以ID：')
    print(id_list)
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        response = requests.post(url=post_url, data=data, headers=headers)
        page_json = response.json()
        print(json.dumps(page_json, indent=4, ensure_ascii=False))

    print('完成！！')
