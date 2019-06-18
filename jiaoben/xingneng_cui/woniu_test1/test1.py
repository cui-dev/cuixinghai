#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 18:41
# @Author  : cui
# @File    : test1.py
import requests
import threading
import time
import random
class Woniu:
    def __init__(self):
        self.sess=requests.session()

    def woniu_page(self):
        begin_time = int(time.time()*1000)
        self.sess.get("http://cuishao:8080/WoniuSales1.4/")
        over_time = int(time.time()*1000)
        print("%s打开网站用时%d毫秒"%(threading.current_thread().getName(),over_time-begin_time))

    def woniu_login(self):
        begin_time = int(time.time()*1000)
        date = {'username':'admin','password':'admin','verifycode':'0000'}
        self.sess.post("http://cuishao:8080/WoniuSales1.4/user/login ",data=date)
        over_time = int(time.time()*1000)
        print("%s登陆网站用时%d毫秒" % (threading.current_thread().getName(), over_time - begin_time))

    def synthesize(self):
        self.woniu_page()
        time.sleep(random.randint(2,4))
        self.woniu_login()

if __name__ == '__main__':
    woniu=Woniu()
    for i in range(10):
        t=threading.Thread(target=woniu.synthesize)
        t.start()
        time.sleep(0.5)




















