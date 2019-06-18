#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
dr=webdriver.Chrome() #驱动服务器
dr.get("http://cuishao:8080/WoniuSales1.4/") #登陆URL
dr.maximize_window()
user=dr.find_element_by_id("username")  #账号
user.click()
user.send_keys("admin")
password=dr.find_element_by_id("password")   #密码
password.click()
password.send_keys("admin")
ver=dr.find_element_by_id("verifycode")  #验证码
ver.click()
ver.send_keys("0000")
dr.find_element_by_xpath("//button[@class = 'form-control btn-primary']").click() #登陆按钮
barcod=dr.find_element_by_id("barcode")  #添加商品
barcod.click()
barcod.send_keys("1234")
dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click() #点击查询按钮
number=dr.find_element_by_xpath("(//option)[1]").text
# discount=dr.find_element_by_xpath("(//input[@type = 'text'])[3]")  #折扣框
# sleep(2)
# discount.click()
# sleep(1)
# discount.send_keys(Keys.CONTROL,'a') #ctrl+a 全选输入框内容
# sleep(1)
# discount.send_keys(Keys.CONTROL,'x')
# sleep(1)
# discount.send_keys("80")
sleep(1)
dr.find_element_by_xpath("//button[@onclick='buyCountPlus(this)']").click() #增加一件商品
sleep(1)
discounts=dr.find_element_by_id("customerphone")  #增加会员
discounts.click()
discounts.send_keys("12222343234")
sleep(1)
dr.find_element_by_id("submit").click() #确认收款
sleep(1)
dr.switch_to.alert.accept()  #alert窗口确定
sleep(1)
barcod=dr.find_element_by_id("barcode")  #添加商品
barcod.click()
barcod.send_keys("1234")
dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click() #点击查询按钮
numbers=dr.find_element_by_xpath("(//option)[1]").text
if numbers != number:
    print("验证通过，不是问题")
else:
    print("验证未通过，是问题")
sleep(3)
#截图
now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
dr.get_screenshot_as_file(".\\"+ now + "error_png.png")#推荐
dr.close()
sleep(2)


#第二次开启服务器
dr=webdriver.Chrome() #驱动服务器
dr.get("http://cuishao:8080/WoniuSales1.4/") #登陆URL
dr.maximize_window()
user=dr.find_element_by_id("username")  #账号
user.click()
user.send_keys("admin")
password=dr.find_element_by_id("password")   #密码
password.click()
password.send_keys("admin")
ver=dr.find_element_by_id("verifycode")  #验证码
ver.click()
ver.send_keys("0000")
sleep(2)
dr.find_element_by_xpath("//button[@class = 'form-control btn-primary']").click() #登陆按钮
for i in range(2):
    arcod=dr.find_element_by_id("barcode")  #添加商品
    sleep(1)
    arcod.click()
    arcod.send_keys("1234")
    dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click() #点击查询按钮
    sleep(1)
tests=dr.find_elements_by_xpath("//a[text()='移除']")
sleep(1)
if len(tests) == 1:
    print("验证通过，不是问题")
else:
    print("验证未通过，是问题")
dr.close()










#

