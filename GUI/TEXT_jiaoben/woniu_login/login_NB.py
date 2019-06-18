#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from GUI.TEXT_jiaoben.read_text.reads import Read
class login:
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.dr.get("http://cuishao:8080/WoniuSales1.4/")
    def account(self):
        self.dr.maximize_window()
        list1=Read().reads("../read_text/1.text")
        user = self.dr.find_element_by_id("username")  # 账号
        user.click()
        user.send_keys(list1[0])
        password = self.dr.find_element_by_id("password")  # 密码
        password.click()
        password.send_keys(list1[1])
        ver = self.dr.find_element_by_id("verifycode")  # 验证码
        ver.click()
        ver.send_keys(list1[2])
        self.dr.find_element_by_xpath("//button[@class = 'form-control btn-primary']").click()  # 登陆按钮
        self.dr.quit()
if __name__ == '__main__':
    login().account()