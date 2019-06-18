#!/usr/bin/env python
#-*- coding:utf-8 -*-
from GUI.framework.method.business.mistake import Mistake
from GUI.framework.method.business.business import login
from GUI.framework.method.business.login import logins
from GUI.framework.method.business.member import Members
from GUI.framework.method.business.number import Number
class advocate:
    #登陆
    def loginse(self,nice,niced):
        logins().account(nice,niced)
    #正常收货
    def correct(self,nice,niced):
        login().add(nice,niced)
    #异常
    def abnormal_one(self,nice,niced):
        Mistake().login_two(nice,niced)
    #添加一件商品
    def addition(self,nice,niced):
        Members().members(nice,niced)
    def numberr(self,nice,niced):
        Number().numbers(nice,niced)



