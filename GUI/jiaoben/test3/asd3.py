#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import  sleep
from random import randint
dr=webdriver.Chrome()
dr.get("http://cuishao/agileone/index.php")
dr.maximize_window() #最大化
x=dr.find_element_by_id("username")
x.click()
x.send_keys("admin")
y=dr.find_element_by_id("password")
y.click()
y.send_keys("admin")
dr.find_element_by_id("login").click()
sleep(2)
dr.find_element_by_xpath('//a[text()="※ 公告管理 ※"]').click()
for i in range(100):
    sleep(0.5)
    dr.find_element_by_xpath('//input[@value ="新建"]').click()
    p=randint(1,1000)
    z=dr.find_element_by_id("headline")
    z.click()
    sleep(0.5)
    z.send_keys(p)
    dr.find_element_by_id("add").click()
    dr.refresh()