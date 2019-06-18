#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/6/14 11:28
# software: PyCharm
from jiaoben.reflex.Calculator import Calculators as cal
class Test:

    def test_add(self):
        result = cal.add(5,3)
        if result == 8:
            print('5 + 3 = 8 test success.')
        else:
            print('5 + 3 != 8 test fail.')

    def test_sub(self):
        result = cal.sub(5,3)
        self.function()
        if result == 2:
            print('5 - 3 = 2 test success.')
        else:
            print('5 - 3 != 2 test fail.')

    def function(self):
        print('I am general method.')


if __name__ == '__main__':
    cal_test = Test()
    method = dir(cal_test)
    print(method)
    for method_name in method:
        if method_name.startswith('test') and hasattr(cal_test,method_name):
            getattr(cal_test,method_name)()
