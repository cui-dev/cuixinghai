#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep
from GUI.framework.method.business.login import logins
class Mistake:
    def login_two(self,nice,niced):
        dr=logins().account(nice,niced)
        for i in nice:
            list3=i.split("=")
            if list3[0] == "monet":
                for i in range(2):
                    arcod = dr.find_element_by_id("barcode")  # 添加商品
                    sleep(1)
                    arcod.click()
                    arcod.send_keys(list3[1])
                    dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click()  # 点击查询按钮
                    sleep(1)
        tests = dr.find_elements_by_xpath("//a[text()='移除']")
        sleep(1)
        dr.close()
        if niced == len(tests):
            print("验证通过，问题")
        else:
            print("验证通过，有问题")
