#!/usr/bin/env python
# coding:utf-8
import os

import requests
from hashlib import md5
from lxml import etree


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post(
            'http://upload.chaojiying.net/Upload/Processing.php',
            data=params,
            files=files,
            headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post(
            'http://upload.chaojiying.net/Upload/ReportError.php',
            data=params,
            headers=self.headers)
        return r.json()


def get_check(path):
    chaojiying = Chaojiying_Client(
        'fly1997',
        '19970223',
        '907208')  # 用户中心>>软件ID 生成一个替换 96001
    img = open(path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要
    # 1902 验证码类型  官方网站>>价格体系
    check_data = chaojiying.PostPic(img, 1902)
    return check_data['pic_str']


if __name__ == '__main__':
    # print(get_check('a.jpg'))
    # print('finished!!')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    page_text = response.text
    # encode('iso-8859-1').decode('gbk') 解决中文乱码神器
    # page_text = page_text.encode('iso-8859-1').decode('gbk')
    tree = etree.HTML(page_text)
    check_url = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    if not os.path.exists('./check'):
        os.mkdir('./check')
    check_data = requests.get(url=check_url, headers=headers).content
    img_path = './check/1.jpg'
    with open(img_path, 'wb') as fp:
        fp.write(check_data)
        print('check_img has been download finish!!')
    print('the check_img information is:', get_check(img_path))
