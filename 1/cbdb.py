# -*- coding: utf-8 -*-
# @Project: 标注工具
# @Author: little fly
# @File name: cbdb
# @Create time: 2020/8/14 16:23
import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
from langconv import *
import xlrd


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    base_url = 'https://cbdb.fas.harvard.edu/cbdbapi/person.php?%20name='
    count = 1
    for path in os.listdir(r'C:\Users\Administrator\Desktop\辉祥'):
        count += 1
        if count < 100:
            continue
        if count > 200:
            break
        document = os.path.join(r'C:\Users\Administrator\Desktop\辉祥', path)
        print(path)
        workbook = xlrd.open_workbook(document)
        table = workbook.sheets()[0]
        name = str(table.cell_value(1, 1))
        name = Converter("zh-hant").convert(name)
        print(name)
        url = base_url + name
        params = {
            'name': name
        }
        response = requests.get(url=url, params=params, headers=headers)
        browser = webdriver.Chrome()
        browser.get(url=url)
        browser.implicitly_wait(10)
        input('enter to next:')
