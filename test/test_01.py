# -*- coding: utf-8 -*-
# @Project  :webUiTest
# @File     :test_01.py
# @Description: 
# @Date     :2021/12/2 17:10
# @Author   :Concon
# @Email    :meetky@sina.cn
# @Software :PyCharm
import time

from driver.driver import Driver
from common.base import Base

driver = Driver()
base = Base(driver.start())
locator = ("xpath", '//*[@id="s-top-left"]/a[6]')
base.find(locator).click()
driver.quit()
