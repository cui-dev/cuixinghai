#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 19:27
# @Author  : cui
# @File    : requests_03.py
from  jiaoben.xingneng.requests.requests_01 import Woniu_Sales
from  jiaoben.xingneng.requests.requests_02 import market_inquire
import unittest
import HTMLTestRunner
from jiaoben.xingneng.zuoye2.login import Wonius
from jiaoben.xingneng.zuoye2.zuoye1 import Woniu
#作为HTML文件报告输出
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Woniu_Sales))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(market_inquire))
with open('test_report.html', 'w') as f:
    runner = HTMLTestRunner.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
    runner.run(suite)