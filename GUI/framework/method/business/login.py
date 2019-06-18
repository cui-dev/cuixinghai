#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep

from selenium import webdriver
class logins:
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.dr.get("http://cuishao:8080/WoniuSales1.4/")
    def account(self,nice,niced):
        for i in nice:
            list2=i.split("=")
            if list2[0] == "user":
                self.dr.maximize_window()
                user = self.dr.find_element_by_id("username")  # 账号
                user.click()
                user.send_keys(list2[1])
            elif list2[0]=="word":
                password = self.dr.find_element_by_id("password")  # 密码
                password.click()
                password.send_keys(list2[1])
            elif list2[0]=="cond":
                ver = self.dr.find_element_by_id("verifycode")  # 验证码
                ver.click()
                ver.send_keys(list2[1])
        self.dr.find_element_by_xpath("//button[@class = 'form-control btn-primary']").click()  # 登陆按钮
            #判断
        sleep(2)
        users=self.dr.find_element_by_xpath("//a[text()='注销']").text
        if users == niced:
            print("登陆成功")
        else:
            print("登录失败")
        return self.dr



