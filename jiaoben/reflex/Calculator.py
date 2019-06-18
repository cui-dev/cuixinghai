#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/6/14 11:25
# software: PyCharm

class calculators:

    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def sub(a,b):
        return a - b

    @staticmethod
    def multi(a,b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    #定义转化数字类型的方法
    @staticmethod
    def aton(sNum):
        if isinstance(sNum,str):
            try:
                return int(sNum)
            except ValueError:
                return float(sNum)
        return sNum
