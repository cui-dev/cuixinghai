#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 17:59
# @Author  : cui
# @File    : have_fun.py
from time import sleep

from selenium import webdriver
class login:
    def __init__(self):
        self.dr=webdriver.Chrome()
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
        self.qiang()
    def qiang(self):
        target1 = self.dr.find_element_by_xpath("//div[@class = 'col-lg-4 col-md-4 col-sm-4 col-xs-4 center']")
        self.dr.execute_script("arguments[0].scrollIntoView();", target1)
        self.dr.find_element_by_xpath('//a[text()="蜗牛学院"]').click()
        nowhandle = self.dr.current_window_handle  # 获得当前句柄
        self.dr.find_element_by_xpath("(//a[text()='精品网课' ])[1]").click()  # 打开另一个窗口网站
        allhandle = self.dr.window_handles  # 获得所有窗口句柄
        for handle in allhandle:
            if handle != nowhandle:
                self.dr.switch_to.window(handle)   #切换窗口
                sleep(3)
        dangqian =self.dr.current_window_handle  #获得当前窗口的句柄
        sleep(5)
        self.dr.find_element_by_xpath("//a[text()='师资介绍']").click()  #点击新的窗口界面
        sleep(5)
        allhandles = self.dr.window_handles #获得所有窗口的句柄
        for newhand in allhandles:  #遍历所有的句柄
            if newhand != dangqian and newhand != nowhandle:  #判断当前句柄是否在界面上应用
                self.dr.switch_to.window(newhand)   #切换窗口





if __name__ == '__main__':
    login().account()
