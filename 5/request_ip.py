# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: request_ip
# @Create time: 2020/8/15 16:34
import re
import telnetlib
import requests
from lxml import etree


base_url = 'https://www.kuaidaili.com/free/inha/%d/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

ip_list = []


def ip_true(ip, port):
    try:
        # ip_http = choice(ip_list)
        # ip = re.findall('http://(.*?):', ip_http)[0]
        # port = re.findall('\d:(.*?)\Z', ip_http)[0]
        # port = str(ip_http).split(':')[2]
        telnetlib.Telnet(ip, port=port, timeout=1)
    except BaseException:
        print('connect failed')
        print('*' * 20)
        return False
    else:
        print('success')
        print('http://' + ip + ':' + port)
        print('*' * 20)
        return True


if __name__ == '__main__':
    try:
        for page in range(49, 100):
            print('------------------第%d页--------------------' % (page))
            url = str(base_url % (page))
            page_text = requests.get(url=url, headers=headers).text
            tree = etree.HTML(page_text)
            table = tree.xpath('//*[@id="list"]/table/tbody/tr')
            for tr in table:
                ip = tr.xpath('./td[1]/text()')[0]
                port = tr.xpath('./td[2]/text()')[0]
                # dic = {"http": ip + ':' + port}
                # print(dic)
                ip_http = 'http://' + ip + ':' + port
                # print(ipstr)
                # ip_list.append(ipstr)
                if ip_true(ip, port):
                    ip_list.append(ip_http)
    except BaseException:
        print('爬取出错！！')
    file = open('可用ip.txt', 'w', encoding='utf-8')
    for data in ip_list:
        file.write("'"+data+"'" + '\n')
