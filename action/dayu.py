#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: dayu.py
@time: 31/01/2018 17:04
"""

import time
import browser
from user_agent import generate_user_agent


dayu_url = 'https://mparticle.uc.cn/article.html?wm_aid='


def act(page, proxy):
    b, session = browser.build_browser(generate_user_agent(), proxy)
    url = dayu_url + page['id']
    b.start_session(session)
    b.get(url)
    time.sleep(1)
