# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: ip代理
# @Create time: 2020/8/14 15:26
import telnetlib

if __name__ == '__main__':
    try:
        telnetlib.Telnet('221.15.192.96', port='1080', timeout=3)
    except:
        print('ip无效！')
    else:
        print('ip有效！')