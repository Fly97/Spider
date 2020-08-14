# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: 5.多协程
# @Create time: 2020/8/14 23:42
import time
import asyncio


async def request(url):
    print('正在下载', url)
    # time.sleep(2)
    await asyncio.sleep(2)
    print('下载成功', url)


if __name__ == '__main__':
    urls = [
        'www.baidu.com',
        'www.sogou.com',
        'www.douban.com'
    ]
    start_time = time.time()
    stasks = []
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        stasks.append(task)
    loop = asyncio.get_event_loop()
    # 需要将任务列表封装到wait中
    loop.run_until_complete(asyncio.wait(stasks))
    print(time.time() - start_time)
