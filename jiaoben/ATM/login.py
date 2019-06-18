#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 12:03
# @Author  : cui
# @File    : login.py
from selenium.webdriver.common.by import By

from jiaoben.ATM.common import Common


class Login:

    #获得driver
    def __init__(self):
        self.driver = Common.get_driver('gc')  #括号中可以写浏览器对象


    #定义必须的方法，完成测试环境准备
    def prepare(self):
        self.driver.get('http://jacky-vpc/agileone')
        if Common.is_element_presence(By.ID,'username') and 'Welcome' in self.driver.title:
            print('准备成功')
            return self.driver
        else:
            print("准备失败")


    #定义必须的方法，完成测试结束资源清理
    def finsh(self):
        pass





