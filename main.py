#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: main.py
@time: 31/01/2018 17:21
"""

import requests
import json
import random
import time
import config
from action import dayu, toutiao

dayu_pages = config.get('channel.dayu.page_ids', [])
toutiao_pages = config.get('channel.toutiao.page_ids', [])
proxies = []


def build_ip_pool():
    global proxies
    resp = requests.get('http://localhost:8000/')
    proxies = json.loads(resp.text)


def valid_proxy(rand_idx):
    rand_proxy = proxies[rand_idx]
    ip = rand_proxy[0]
    port = rand_proxy[1]
    proxy_obj = {"http": "http://%s:%s" % (ip, port), "https": "http://%s:%s" % (ip, port)}
    resp = requests.get('https://www.baidu.com', proxies=proxy_obj, timeout=5)
    return len(resp.text) > 100


if __name__ == '__main__':
    build_ip_pool()
    visit_num = 0
    while True:
        time.sleep(random.randint(2, 5))
        rand_idx = random.randint(0, len(proxies)-1)
        http_proxy = '%s:%s' % (proxies[rand_idx][0], proxies[rand_idx][1])
        try:
            if not valid_proxy(rand_idx):
                continue
            print('%d Visiting...' % visit_num)
            visit_num += 1
            print('     Visiting Dayu...')
            for page_id in dayu_pages:
                dayu.act({'id': page_id}, http_proxy)
            print('     Visiting Toutiao...')
            for page_id in toutiao_pages:
                toutiao.act({'id': page_id}, http_proxy)

        except Exception as e:
            print(e)
            del proxies[rand_idx]
