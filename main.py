#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: main.py
@time: 31/01/2018 17:21
"""

import threading
import requests
import json
import config
from action import dayu, toutiao
from channel import Channel

dayu_pages = config.get('channel.dayu.page_ids', [])
toutiao_pages = config.get('channel.toutiao.page_ids', [])
proxies = []


def build_ip_pool():
    global proxies
    resp = requests.get('http://localhost:8000/')
    proxies = json.loads(resp.text)


if __name__ == '__main__':
    build_ip_pool()
    visit_num = 0
    lock = threading.Lock()
    channels = [Channel('dayu', lock, proxies, dayu, dayu_pages),
                Channel('toutiao', lock, proxies, toutiao, toutiao_pages)]
    for t in channels:
        t.start()
    for t in channels:
        t.join()

