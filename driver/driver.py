# -*- coding: utf-8 -*-
# @Project  :webUiTest
# @File     :driver.py
# @Description: 
# @Date     :2021/12/2 16:58
# @Author   :Concon
# @Email    :meetky@sina.cn
# @Software :PyCharm
import time

from selenium import webdriver


class Driver():
    _url = "http://www.baidu.com"

    def start(self):
        self._driver = webdriver.Chrome()
        self._driver.get(self._url)
        self._driver.maximize_window()
        return self._driver

    def quit(self):
        time.sleep(2)
        return self._driver.quit()
