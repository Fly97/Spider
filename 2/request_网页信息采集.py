# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: request_网页信息采集
# @Create time: 2020/8/12 22:43
import requests

if __name__ == '__main__':
    # UA伪装:将User-Agent封装到字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    kw = input('enter a word:')
    # 将请求数据封装到字典中
    param = {
        'query': kw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    file_name = './html_list/'+kw + '.html'
    with open(file_name, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据成功！')
