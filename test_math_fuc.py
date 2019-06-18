#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from parameterized import parameterized

from training.phase7.API_Testing import test_func_1
from training.phase7.API_Testing.math_func import MathFunc
import os
import HTMLTestRunner


class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.math = MathFunc()
        # print('********** setUpClass execute **********')

    # @classmethod
    # def tearDownClass(cls):
    #     # print('********** tearDownClass execute **********')
    #     pass
    #
    # def setUp(self):
    #     # print('********** setUp execute **********')
    #     pass
    #
    # def tearDown(self):
    #     # print('********** tearDown execute **********')
    #     pass

    def test_add(self):
        # print('********** test_add execute **********')
        list = [(2, 3, 5), (0, 1, 0), (5, 6, 10), (-1, 1, 0)]
        errors = []
        for li in list:
            a, b, expect = li
            try:
                actual = self.math.add(a, b)
                self.assertEqual(expect, actual)
            except Exception as e:
                errors.append(('%d + %d expect %d' % (a, b, expect), e))
        raise AssertionError(errors)

    @parameterized.expand([(9, 2, 7), (1, -1, 2), (1, 0, 0), (10, 10, 0)])
    def test_sub(self, a, b, expect):
        # print('********** test_sub execute **********')
        actual = self.math.sub(a, b)
        self.assertEqual(expect, actual)

    @parameterized.expand([('2*3=6', 2, 3, 6), ('0*5=1', 0, 5, 1), ('-1*9=-9', -1, 9, -9)])
    def test_mult(self, a, b, expect):
        # print('********** test_mult execute **********')
        actual = self.math.mult(a, b)
        self.assertEqual(expect, actual)


    # @unittest.skip('方法代码待完善')
    # @unittest.skipIf(2 > 3, '方法代码待完善')
    @unittest.skipUnless(False, '方法代码待完善')
    def test_div(self):
        # self.skipTest('方法代码待完善')
        # print('********** test_div execute **********')
        actual = self.math.div(30, 5)
        self.assertEqual(3, actual)


def method1():
    # 最基本的使用方法，注意verbosity参数，它有3个值，大家要明白这三个值的区别。
    unittest.main(verbosity=2)


def method2():
    # 基本等价于method1方法。但是我们要注意测试方法的执行顺序，这个方法示例告诉我们可以自己调整测试顺序。
    # 而method1的测试方法执行顺序是无法调整的。
    suite = unittest.TestSuite()
    suite.addTests([TestMathFunc('test_div'), TestMathFunc('test_sub'),
                    TestMathFunc('test_mult'), TestMathFunc('test_add')])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def method3():
    # 对于测试用例我们可以象method2那样一次性添加，也可以象下面这样一个一个的填。
    # 这里需要注意的是addTest的单复数形式
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunc('test_add'))
    suite.addTest(TestMathFunc('test_mult'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def method4():
    # 利用TestLoader的loadTestsFromName方法来添加测试用例
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_math_fuc.TestMathFunc'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def method5():
    # 利用TestLoder的loadTestsFromNames方法来添加测试用例
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_math_fuc.TestMathFunc',
                                                             'test_func_1.TestFunction']))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def method6():
    suite = unittest.TestSuite()
    # 注意defaultTestLoader和TestLoad之间的异同
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathFunc))
    # 下面这个用法是一种变形用法
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(test_func_1.TestFunction))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def method7():
    # 使用unittest的makeSuite方法也可以添加测试用例，
    # 目前这个方法pycharm提示找不到，可能新版本会有变化，以后还是慎用为好。
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestMathFunc))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def method8():
    # 这个方法主要体现TestResult的用法
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathFunc))
    result = unittest.TestResult(verbosity=2)
    suite.run(result)
    print('failures:', result.failures)
    print('errors:', result.errors)
    print('testsRun:', result.testsRun)


def method9():
    # 利用discover方法自动在指定目录下搜索测试用例并添加到TestSuite中
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.discover(os.getcwd(), 'test*.py'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def method10():
    # 将测试结果保存到文本文件中
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathFunc))
    with open('test_report.txt', 'w', encoding='utf8') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)


def method11():
    # 将测试结果利用HTMLTestRunner这一第三方库来生成HTML格式的测试报告。
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestMathFunc))
    with open('test_report.html', 'w', encoding='utf8') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='unittest demo report', verbosity=2)
        runner.run(suite)


if __name__ == '__main__':
    method1()
