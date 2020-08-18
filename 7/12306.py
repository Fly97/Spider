# -*- coding: utf-8 -*-
# @Project: Spider
# @Author: little fly
# @File name: 12306
# @Create time: 2020/8/17 12:06
import requests
from selenium import webdriver
from PIL import Image
from hashlib import md5
import time
from selenium.webdriver import ActionChains


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
    check_data = chaojiying.PostPic(img, 9004)
    return check_data['pic_str']


if __name__ == '__main__':
    url = 'https://kyfw.12306.cn/otn/resources/login.html'
    chrom = webdriver.Chrome()
    chrom.maximize_window()
    chrom.get(url)
    time.sleep(1)
    # page_text = chrom.page_source
    # print(page_text)
    chrom.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()

    chrom.save_screenshot('./check/aa.png')
    code_img_ele = chrom.find_element_by_xpath('//*[@id="J-loginImg"]')
    img_location = code_img_ele.location
    img_size = code_img_ele.size
    rangle = (int(img_location['x']),
              int(img_location['y']),
              int(img_location['x']) + int(img_size['width']),
              int(img_location['y']) + int(img_size['height']))
    print(rangle)
    aa = Image.open('./check/aa.png')
    frame = aa.crop(rangle)
    frame.save('./check/code.png')
    code = get_check('./check/code.png')
    print(code)
    signs = str(code).split('|')
    for sign in signs:
        if len(sign.split(',')) < 2:
            continue
        x = int(sign.split(',')[0])
        y = int(sign.split(',')[1])
        ActionChains(chrom).move_to_element_with_offset(
            code_img_ele, x, y).click().perform()
        time.sleep(0.5)
    chrom.find_element_by_xpath(
        '//*[@id="J-userName"]').send_keys('www.zhangbowudi@qq.com')
    time.sleep(2)
    chrom.find_element_by_xpath(
        '//*[@id="J-password"]').send_keys('bobo_15027900535')
    time.sleep(2)
    chrom.find_element_by_xpath('//*[@id="J-login"]').click()

    # time.sleep(4)
    # chrom.save_screenshot('./check/bb.png')
    # chrom.refresh()
    time.sleep(2)
    # iframe = chrom.find_element_by_xpath('//iframe')
    # chrom.switch_to.frame('xh-bar')
    # print(chrom.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span/text()'))
    try:
        drag = chrom.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        action = ActionChains(chrom)
        action.click_and_hold(drag).perform()
        for i in range(10):
            # perform()立即执行动作链操作
            # move_by_offset(x,y):x水平方向 y竖直方向
            action.move_by_offset(20, 0).perform()
            time.sleep(0.5)
        action.release()
    except BaseException:
        print(BaseException)
    time.sleep(10)
    chrom.quit()
    print('完成！！')
