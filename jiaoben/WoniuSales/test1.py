#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 21:02
# @Author  : cui
# @File    : test1.py

from time import sleep

from selenium import webdriver
class login:
    def __init__(self):
        self.dr=webdriver.Firefox()
        self.dr.get("http://cuishao:8080/WoniuSales1.4/")
        self.dr.maximize_window()
    def account(self):
        user = self.dr.find_element_by_id("username")  # 账号
        user.click()
        user.send_keys("admin")
        password = self.dr.find_element_by_id("password")  # 密码
        password.click()
        password.send_keys("admin")
        ver = self.dr.find_element_by_id("verifycode")  # 验证码
        ver.click()
        ver.send_keys("0000")
        self.dr.find_element_by_xpath("//button[@class = 'form-control btn-primary']").click()  # 登陆按钮
        sleep(3)
        #write
        # self.dr.execute_script("document.getElementById('newcredit').readOnly=true;")
        self.dr.execute_script("document.getElementById('newcredit').removeAttribute('readonly');")


        sleep(10)

if __name__ == '__main__':
    login().account()