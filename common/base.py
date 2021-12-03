# -*- coding: utf-8 -*-
# @Project  :webUiTest
# @File     :base.py
# @Description: 
# @Date     :2021/12/2 16:27
# @Author   :Concon
# @Email    :meetky@sina.cn
# @Software :PyCharm
from selenium.webdriver.chrome.webdriver import WebDriver


class Base:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def find(self, locator):
        """
            查找元素
        """
        return self._driver.find_element(*self._parse(locator))

    def _parse(self, locator, value=None):
        """
            解析元素定位方式，可传数组
        :param locator: 定位方式
        :param value: 元素路径
        :return: (定位方式,元素路径)
        """
        # 判断入参类型，若为元组类型，则解包
        if isinstance(locator, tuple):
            value = locator[1]
            locator = locator[0]
        else:
            pass
        if locator == "id":
            return locator, value

        if locator == "xpath":
            return locator, value

    def click(self):
        pass


if __name__ == '__main__':
    pass
