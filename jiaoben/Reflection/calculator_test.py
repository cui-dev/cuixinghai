#! /usr/bin/env python
# -*- coding: utf-8 -*-
from jiaoben.Reflection.calculator import Calculator as cal


class CalculatorTest:

    def test_add(self):
        result = cal.add(5, 3)
        if result == 8:
            print('5 + 3 = 8 test success.')
        else:
            print('5 + 3 != 8 test fail.')

    def test_sub(self):
        result = cal.sub(5, 1)
        self.function()
        if result == 2:
            print('5 - 3 = 2 test success.')
        else:
            print('5 - 3 != 2 test fail.')

    def function(self):
        print('i am general method.')


if __name__ == '__main__':
    cal_test = CalculatorTest()
    methods = dir(cal_test)
    for method_name in methods:
        if method_name.startswith('test') and hasattr(cal_test, method_name):
            getattr(cal_test, method_name)()
