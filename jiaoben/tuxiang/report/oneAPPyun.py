#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 11:44
# @Author  : cui
# @File    : oneAPPyun.py

from appium import webdriver
import os,time

class OneStrokTest:

    def __init__(self):
        app_path = os.path.join(os.getcwd(),'yibijizhang.apk')
        desred_caps = {
            'platformName': 'Android',
            'platfromVersion': '5.0.2',
            'deviceName': 'Android_5.0',
            'appPackage': 'com',
            'appActivity': 'com',
            'app': app_path,
            'unicodeKeyboard':'True',
            'noReset':'True'}


        url = 'http://127.0.0.1:4723/wd/hub'
        self.driver = webdriver.Remote(url,desred_caps)
        self.driver.implicitly_wait(20)

    def start_app(self):
        self.driver.find_element_by_android_uiautomator('text("记一笔")').click()#文本定位
        one=self.driver.find_element_by_android_uiautomator('text("医疗")')#文本定位
        two=self.driver.find_element_by_android_uiautomator('text("餐饮")')#文本定位
        self.driver.scroll(one,two)  #滚动，两个参数，从哪儿滚动到哪儿
