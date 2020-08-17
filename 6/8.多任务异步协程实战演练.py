import requests
from lxml import etree
import time
import os
import aiohttp
import asyncio
from random import choice

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
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
if not os.path.exists('./picture/fengjing'):
    os.mkdir('./picture/fengjing')
base_pic_path = './picture/fengjing/'


async def get_picture(dic):
    url = dic['url']
    pic_path = base_pic_path + dic['name']
    async with aiohttp.ClientSession() as session:
        # get()、post():
        # headers,params/data,proxy='http://ip:port'
        proxy = choice(ip_list)
        async with await session.get(url=url, proxy=proxy, headers=headers) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            # 注意：获取响应数据操作之前一定要使用await进行手动挂起
            pic_data = await response.read()
            await asyncio.sleep(1)
            with open(pic_path, 'wb') as fp:
                fp.write(pic_data)
                print(dic['name'], '下载成功')


if __name__ == '__main__':
    start = time.time()
    url = 'http://pic.netbian.com/4kfengjing/index_%d.html'
    tasks = []
    for page in range(2, 50):
        new_url = format(url % page)
        # proxy = choice(ip_list)
        page_text = requests.get(url=new_url, headers=headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//div[@class="slist"]/ul/li')
        for li in li_list:
            img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
            name = img_src.split('/')[-1]
            # data = requests.get(url=img_src).content
            # path = './libs/'+name
            # with open(path,'wb') as fp:
            #     fp.write(data)
            #     print(name,'下载成功')
            dic = {
                'name': name,
                'url': img_src
            }
            c = get_picture(dic)
            task = asyncio.ensure_future(c)
            tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('总耗时：', time.time() - start)
