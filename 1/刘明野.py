# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: my_re
# @Create time: 2020/8/14 11:12
import re
import requests
from selenium import webdriver
import time
from lxml import etree

# 实现无可视化界面
from selenium.webdriver.chrome.options import Options

# 实现规避检测
from selenium.webdriver import ChromeOptions

# 实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

# 如何实现让selenium规避被检测到的风险
# bro = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options, options=option)


if __name__ == '__main__':
    # headers = {
    #     'Cookie': 'myfreemp3_lang=en-us',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    # }
    url = 'http://tool.liumingye.cn/music/?page=audioPage&type=migu&name=%E5%91%A8%E6%9D%B0%E4%BC%A6'
    # response = requests.get(url=url, headers=headers)
    # page_text = response.text
    # with open('zjl.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page_text)
    # print('finished!!')

    chorm = webdriver.Chrome(
        executable_path=r'D:\tools\chromedriver.exe',
        # chrome_options=chrome_options,
        options=option)
    chorm.maximize_window()
    chorm.get(url)
    chorm.implicitly_wait(10)
    page_text = chorm.page_source
    # with open('zjl.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="player"]/div[1]/ol/li')
    # try:
    for i, li in enumerate(li_list):
        if i < 8:
            continue
        sing = li.xpath('./span[4]/text()')[0]
        name = li.xpath('./span[5]/text()')[0]
        # print(name, sing)
        xp = str('//*[@id="player"]/div[1]/ol/li[%d]/span[1]' % (i + 1))
        chorm.find_element_by_xpath(xp).click()
        print('click %s success!' % (sing))
        chorm.implicitly_wait(10)
        # chorm.find_element_by_xpath('//*[@id="m-download"]/div/div/div[1]/button').click()
        url = tree.xpath('//*[@id="m-download"]/div/div/div[2]/div[4]/div[2]/a[1]/@href')
        print(name, sing, url)
        # chorm.refresh()
        # chorm.back()
        # chorm.execute_script('document.getElementByClass("btn btn-primary").click()')
        # button = chorm.find_element_by_xpath('//*[@id="m-download"]/div/div/div[3]/button')
        # chorm.execute_script("arguments[0].click();", button)

        print(chorm.find_element_by_xpath('//*[@id="m-download"]/div/div/div[3]/button/text()'))
        button = chorm.find_element_by_xpath('//*[@id="m-download"]/div/div/div[3]/button')
        chorm.execute_script("$(arguments[0]).click()", button)

        chorm.implicitly_wait(10)
        if (i+1) % 10 == 0:
            js = 'var q=document.documentElement.scrollTop=8000'
            chorm.execute_script(js)
            if chorm.find_element_by_xpath('//*[@id="player"]/div[2]'):
                chorm.find_element_by_xpath('//*[@id="player"]/div[2]').click()
    # except BaseException as e:
    #     print('爬取出错：', e)
    # else:
    #     print('finished!!')
    chorm.quit()
