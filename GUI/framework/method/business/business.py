#!/usr/bin/env python
#-*- coding:utf-8 -*-
from GUI.framework.method.business.login import logins
from time import sleep
from random import randint
class login:
    def add(self,nice,niced):
        dr=logins().account(nice,niced)
        for i in nice:
            list1=i.split("=")
            if list1[0] == "monet" :
                barcod = dr.find_element_by_id("barcode")  # 添加商品
                barcod.click()
                barcod.send_keys(list1[1])
                dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click()  # 点击查询按钮
                dr.find_element_by_id("submit").click()  # 确认收款
                sleep(2)
                dr.switch_to.alert.accept()  # alert窗口确定
                sleep(1)
                dr.switch_to.alert.accept()  # alert窗口确定
                if niced == "请确认你已经真实收到":
                    print("验证通过，不是问题")
                else:
                    print("验证未通过，是问题")
        dr.close()







