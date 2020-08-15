# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: dailiyanzheng
# @Create time: 2020/8/15 13:31
import telnetlib
from random import choice
import re



ip_list = [
    'http://196.52.58.239:80',
    'http://165.225.112.77:10605',
    'http://165.225.76.70:10605',
    'http://122.226.57.70:8888',
    'http://123.57.84.116:8118',
    'http://202.109.157.64:9000',
    'http://139.155.41.15:8118',
    'http://39.106.223.134:80',
    'http://47.115.63.52:8888'
]


if __name__ == '__main__':
    for ip_http in ip_list:
        try:
            # ip_http = choice(ip_list)
            ip = re.findall('http://(.*?):', ip_http)[0]
            port = re.findall('\d:(.*?)\Z', ip_http)[0]
            # port = str(ip_http).split(':')[2]
            print('ip:', ip, '\nport:', port)
            telnetlib.Telnet(ip, port=port, timeout=2)
        except BaseException:
            print('connect failed')
            print('*'*20)
        else:
            print('success')
            print(ip_http)
            print('*' * 20)
