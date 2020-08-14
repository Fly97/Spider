# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: 1zhengze_img
# @Create time: 2020/8/13 12:38
import requests

# 爬取图片
if __name__ == '__main__':
    url = 'https://pic.qiushibaike.com/system/pictures/12346/123462218/medium/ISP1BAN0KSLVO4W0.jpg'
    response = requests.get(url=url)
    # content 返回二进制数据
    img_data = response.content
    with open('./document/qiutu.jpg', 'wb') as fw:
        fw.write(img_data)
    print('finished!!!!')
