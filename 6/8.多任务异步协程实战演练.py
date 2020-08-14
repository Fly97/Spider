import requests
from lxml import etree
import time
import os
import aiohttp
import asyncio

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
if not os.path.exists('./picture'):
    os.mkdir('./picture')


async def get_picture(dic):
    url = dic['url']
    pic_path = './picture/' + dic['name'] + '.jpg'
    async with aiohttp.ClientSession() as session:
        # get()、post():
        # headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            # 注意：获取响应数据操作之前一定要使用await进行手动挂起
            pic_data = await response.read()
            with open(pic_path, 'wb') as fp:
                fp.write(pic_data)
                print(dic['name'], '下载成功')


if __name__ == '__main__':
    start = time.time()
    url = 'http://pic.netbian.com/4kmeinv/index_%d.html'
    tasks = []
    for page in range(2, 50):
        new_url = format(url % page)
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
