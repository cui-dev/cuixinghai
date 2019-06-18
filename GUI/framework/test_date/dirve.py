#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from GUI.framework.method.public.read_csv import Reads
class Driver:
    def driver_it(self):
        table = Reads().reade('../test_date/datas.csv')
        for list in range(1,len(table)):
            print("########开始执行测试用例%s########" %table[list][0])
            __import__('GUI.framework.test_case.' + table[list][1]) #动态导入模块
            module = sys.modules['GUI.framework.test_case.' + table[list][1]] #把模块加入内存
            c = getattr(module,table[list][2])#获取到类,类反射:getattr(object,str)获取对象属性值
            obj = c()#实例化类
            method = getattr(obj,table[list][3])#获取到方法
            parameters = table[list][4].split('\n')#以回车分割，转换为列表返回
            method(parameters,table[list][5])
            print("########完成执行测试用例%s########" %table[list][0])

if __name__ == '__main__':
    Driver().driver_it()