#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from random import randint
class login:
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.dr.get("http://cuishao:8080/WoniuSales1.4/")
    def account(self):
        self.dr.maximize_window()
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
    def add(self):
        barcod = self.dr.find_element_by_id("barcode")  # 添加商品
        barcod.click()
        barcod.send_keys("1234")
        self.dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click()  # 点击查询按钮
    def increase(self):
        num=''
        for i in range(11):
            number=str(randint(0,9))
            num+=number
        self.dr.find_element_by_xpath("//button[@onclick='buyCountPlus(this)']").click()  # 增加一件商品
        discounts = self.dr.find_element_by_id("customerphone")  # 增加会员
        discounts.click()
        discounts.send_keys(num)
    def money(self):
        number = self.dr.find_element_by_xpath("(//option)[1]").text
        self.dr.find_element_by_id("submit").click()  # 确认收款
        sleep(2)
        self.dr.switch_to.alert.accept()  # alert窗口确定
        numbers = self.dr.find_element_by_xpath("(//option)[1]").text
        if numbers != number:
            print("验证通过，不是问题")
        else:
            print("验证未通过，是问题")
        sleep(3)
        self.dr.refresh()    #刷新页面
    ##逆向操作
    def login_two(self):
        for i in range(2):
            arcod = self.dr.find_element_by_id("barcode")  # 添加商品
            sleep(1)
            arcod.click()
            arcod.send_keys("1234")
            self.dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click()  # 点击查询按钮
            sleep(1)
        tests = self.dr.find_elements_by_xpath("//a[text()='移除']")
        sleep(1)
        if len(tests) == 1:
            print("验证通过，不是问题")
        else:
            print("验证未通过，是问题")
        self.dr.close()


if __name__ == '__main__':
    a=login()
    sleep(2)
    a.account()
    sleep(2)
    a.add()
    sleep(2)
    a.increase()
    sleep(2)
    a.money()
    sleep(1)
    a.login_two()