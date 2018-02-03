#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: browser.py
@time: 31/01/2018 17:09
"""

import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType

driver = webdriver.PhantomJS(executable_path=config.get('driver.path', '/usr/local/bin/phantomjs'))
driver.implicitly_wait(3)
driver.set_page_load_timeout(8)
driver.set_script_timeout(10)


def build_browser(agent, http_proxy):
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    desired_capabilities["phantomjs.page.settings.userAgent"] = agent
    desired_capabilities["phantomjs.page.settings.loadImages"] = False

    proxy = webdriver.Proxy()
    proxy.proxy_type = ProxyType.MANUAL

    proxy.http_proxy = http_proxy
    proxy.add_to_capabilities(desired_capabilities)
    return driver, desired_capabilities
