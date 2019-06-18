#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import  sleep
dr = webdriver.Chrome()   #获取对应的浏览器
dr.maximize_window() #窗口最大化
dr.get("http://cuishao:8080/WoniuSales1.4/") #打开网址
dr.find_element_by_id("username").click()#定位单击输入框
sleep(2)  #等待两秒
dr.find_element_by_id("username").send_keys("admin")#输入内容
sleep(2)
dr.find_element_by_id("password").click()#定位密码输入框
dr.find_element_by_id("password").send_keys("admin")#密码
sleep(2)
dr.find_element_by_id("verifycode").click()#定位验证码输入框
dr.find_element_by_id("verifycode").send_keys("0000")#输入验证码
sleep(2)
dr.find_element_by_xpath("//*[@type = 'button' and @class ='form-control btn-primary']").click()
sleep(1)
if dr.title =="蜗牛进销存-销售出库":
    print("登陆成功")
else:
    print("登陆失败")
dr.find_element_by_id("barcode").click() #找到商品条码框
dr.find_element_by_id("barcode").send_keys("1234")
dr.find_element_by_xpath("//*[@class='form-control btn-primary']").click()
sleep(1)
dr.find_element_by_id("goodssizeList").click() #单击下拉框
dr.find_element_by_xpath("//*[@id='goodssizeList']/option[2]") .click() #选择第二个
#界面崩溃
# dr.find_element_by_xpath("(//input[@type = 'text'])[3]").click()
# sleep(2)
# dr.find_element_by_xpath("(//input[@type = 'text'])[3]").clear()
########
dr.find_element_by_xpath("//button[@onclick ='buyCountPlus(this)']").click()













sleep(5)
dr.find_element_by_xpath("(//input[@type = 'text'])[3]").send_keys("80")
sleep(1)
dr.find_element_by_xpath("//*[@id='goodslist']/tr/td[8]/button[2]").click()
dr.find_element_by_xpath("//*[@class = 'form-control btn-block btn-primary']").click()
sleep(1)
dr.switch_to.alert.accept()
sleep(1)
dr.switch_to.alert.accept()



