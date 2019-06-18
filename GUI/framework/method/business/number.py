#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep

from GUI.framework.method.business.login import logins
class Number:
    def numbers(self,nice,niced):
        dr=logins().account(nice,niced)
        for i in nice:
            list5=i.split("=")
            if list5[0] == "monet":
                barcod = dr.find_element_by_id("barcode")  # 添加商品
                barcod.click()
                barcod.send_keys(list5[1])
            elif list5[0] == "monets":
                barcod = dr.find_element_by_id("barcode")  # 添加商品
                barcod.click()
                barcod.send_keys(list5[1])
        sleep(1)
        tests = dr.find_elements_by_xpath("//a[text()='移除']")
        dr.close()

        #断言
        if niced == str(tests):
            print("验证通过，没问题")
        else:
            print("验证没通过，有问题")
