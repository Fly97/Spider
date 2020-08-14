# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: 6.多协程2
# @Create time: 2020/8/15 0:02
import requests
import asyncio
import time
import aiohttp


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # get()、post():
        # headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            # 注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)


if __name__ == '__main__':
    urls = [
        'http://127.0.0.1:5000/zhx',
        'http://127.0.0.1:5000/lst',
        'http://127.0.0.1:5000/zxy'
    ]
    start_time = time.time()
    tasks = []
    for url in urls:
        c = get_page(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    # 需要将任务列表封装到wait中
    loop.run_until_complete(asyncio.wait(tasks))
    print('all_time:', time.time() - start_time)
