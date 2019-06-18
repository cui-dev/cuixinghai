#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import  sleep
from random import randint
from jiaoben.test3.mysql import *
class delete:
    def __init__(self):
        self.dr=webdriver.Chrome()
        self.dr.get("http://cuishao/agileone/index.php")
        self.list1=[]#存放数据库ID
    def login(self):
        self.dr.maximize_window() #最大化
        x=self.dr.find_element_by_id("username")
        x.click()
        x.send_keys("admin")
        y=self.dr.find_element_by_id("password")
        y.click()
        y.send_keys("admin")
        self.dr.find_element_by_id("login").click()
        sleep(2)
        self.dr.find_element_by_xpath("//a[text()='※ 公告管理 ※']").click()

    def reads(self):
        p = seek("select noticeid from notice")  # 获取数据库
        for i in p:  # 遍历数据库ID
            self.list1.append(i[0])
        number = len(self.list1) - 1
        numbers = randint(1, number)
        self.login()
        while 1 :
            list2=[]
            sleep(2)
            for j in range(1, 31): #遍历编号
                a = int(self.dr.find_element_by_xpath("(//label[@onclick= 'goEdit(this,false)'])[%d]" % (j)).text)  #获取编号数值
                list2.append(a)  #加到列表当中
            while 1:
                sleep(2)
                print(numbers)
                if numbers in list2:  #判断number在没在list2中
                    sleep(2)
                    numberss = list2.index(numbers)+1   #获取在list2中的下标
                    print(numberss)
                    self.dr.find_element_by_xpath("(//label[@onclick= 'doDelete(this)'])[%d]" % (numberss)).click()  #下标赋值给删除
                    sleep(2)
                    self.dr.switch_to.alert.accept() #点击确定
                    exit("牛逼")
                else:
                    self.dr.find_element_by_xpath("//img[@src = '/agileone/Common/Image/next.gif']").click()  #翻页且清空列表
                    sleep(2)
                    break

        # target1 = self.dr.find_element_by_xpath("//*[text()='页顶']")
        # self.dr.execute_script("arguments[0].scrollIntoView();", target1)
        # sleep(3)
        # target2 = self.dr.find_element_by_xpath("(//input[@type = 'button'])[2]")
        # self.dr.execute_script("arguments[0].scrollIntoView();", target2)





if __name__ == '__main__':
    o=delete()
    o.reads()
