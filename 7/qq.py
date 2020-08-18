# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: qq
# @Create time: 2020/8/17 18:17
import requests
from selenium import webdriver
from PIL import Image
from hashlib import md5
import time
from selenium.webdriver import ActionChains


if __name__ == '__main__':
    url = 'http://sc.chinaz.com/tupian/fengjingtupian.html'
    chrom = webdriver.Chrome()
    chrom.maximize_window()
    chrom.get(url)
    for i in range(10):
        chrom.forward()
        divs = chrom.find_elements_by_xpath('//*[@id="container"]//a/img')
        for div in divs:
            print(div.get_attribute('src'))