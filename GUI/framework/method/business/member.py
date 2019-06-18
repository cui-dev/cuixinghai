#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep

from GUI.framework.method.business.login import logins
class Members:
    def members(self,nice,niced):
        dr=logins().account(nice,niced)
        for i in nice:
            list4=i.split("=")
            if list4[0] == "monet":
                barcod = dr.find_element_by_id("barcode")  # 添加商品
                barcod.click()
                barcod.send_keys(list4[1])
                dr.find_element_by_xpath("(//button[@class='form-control btn-primary'])[1]").click()  # 点击查询按钮
                tests = dr.find_elements_by_xpath("//a[text()='移除']")
                sleep(2)
                dr.close()

                    #断言
                if niced == str(len(tests)):
                    print("验证通过，没问题")
                else:
                    print("验证失败，有问题")
