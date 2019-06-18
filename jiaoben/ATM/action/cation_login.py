#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 18:12
# @Author  : cui
# @File    : cation_login.py


# 定义一个action组件，执行的动作
from jiaoben.ATM.common import Common
class Do_login:
    def do_login(self, username, password,driver):
        user = driver.find_element_by_id('username')
        user.clear()
        user.send_keys(username)
        word = driver.find_element_by_id('password')
        word.clear()
        word.send_keys(password)
        driver.find_element_by_id('login').click()
        Common.random_sleep()