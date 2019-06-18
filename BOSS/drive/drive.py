#!/usr/bin/env python
#-*- coding:utf-8 -*-

import HTMLTestRunner
import unittest


suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase())
with open('./HTMLReport/Test_Report.html', 'w') as f:
    runner = HTMLTestRunner.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
    runner.run(suite)
