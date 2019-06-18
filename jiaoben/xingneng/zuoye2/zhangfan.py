#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 20:54
# @Author  : cui
# @File    : zhangfan.py
import unittest
import HTMLTestRunner
from jiaoben.xingneng.zuoye2.login import Wonius
from jiaoben.xingneng.zuoye2.zuoye1 import Woniu
#作为HTML文件报告输出
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Woniu))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Wonius))
with open('test_report.html', 'w') as f:
    runner = HTMLTestRunner.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
    runner.run(suite)

