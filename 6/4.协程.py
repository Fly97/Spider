# -*- coding: utf-8 -*-
# @Project: Spider_Hero
# @Author: little fly
# @File name: 4.协程
# @Create time: 2020/8/14 23:24
import asyncio


async def request(url):
    print('正在请求url:', url)
    print('请求成功')
    return url


def callback_func(task):
    print(task.result())


if __name__ == '__main__':
    c = request('www.baidu.com')
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(c)

    # loop = asyncio.get_event_loop()
    # task = loop.create_task(c)
    # print(task)
    # loop.run_until_complete(task)
    # print(task)

    # loop = asyncio.get_event_loop()
    # future = asyncio.ensure_future(c)
    # print(future)
    # loop.run_until_complete(future)
    # print(future)

    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(c)
    task.add_done_callback(callback_func)
    loop.run_until_complete(task)
