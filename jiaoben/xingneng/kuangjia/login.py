#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
class Login(unittest.TestCase):
    # def setUp(self):
    #     print("yes")

    def test1(self):
        print("123")

    def test2(self):
        print("1234")

# if __name__ == '__main__':
    # 方法11：html测试报告
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Login))
with open('test_report.html', 'w') as f:
    runner = HTMLTestRunner.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
    runner.run(suite)


