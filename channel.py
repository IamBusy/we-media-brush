#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: channel.py
@time: 03/02/2018 13:26
"""

import threading
import random
import requests


class Channel(threading.Thread):
    def __init__(self, name, lock, proxies, actor, pages):
        threading.Thread.__init__(self)
        self.actor = actor
        self.pages = pages
        self.lock = lock
        self.proxies = proxies
        self.name = name

    def get_proxy(self):
        self.lock.acquire()
        while True:
            rand_idx = random.randint(0, len(self.proxies) - 1)
            try:
                proxy = self.proxies[rand_idx]
                ip = proxy[0]
                port = proxy[1]
                proxy_obj = {"http": "http://%s:%s" % (ip, port), "https": "http://%s:%s" % (ip, port)}
                resp = requests.get('https://www.baidu.com', proxies=proxy_obj, timeout=3)
                if len(resp.text) > 100:
                    self.lock.release()
                    return proxy
            except Exception as e:
                del self.proxies[rand_idx]

    def run(self):
        print('Start thread...')
        proxy = self.get_proxy()
        http_proxy = '%s:%s' % (proxy[0], proxy[1])
        num = 0
        while True:
            print('[%s] visiting: %d' % (self.name, num))
            num += 1
            for page_id in self.pages:
                self.actor.act({'id': page_id}, http_proxy)


