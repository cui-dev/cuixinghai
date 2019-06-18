#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
class Sky(unittest.TestCase):
    #类里面的方法执行顺序跟位置没有关系，可以任意放置
    #setUpClass、setUp、tearDown、tearDownClass,非必须，可有可无，根据你的需要

    @classmethod#这个注解必须，不然会报错
    def setUpClass(cls):#在所有test开头的方法执行之前只执行一次
        print("I am setUpClass!")

    def setUp(self):#每个test开头的方法运行之前都会执行一次
        print("I am setUp!")

    def test2(self):#必须以test开头的方法（小写）才能运行;运行顺序遵循Ascii码:先数字，在大写字母，最后小写字母
        print("I am test2!")

    def test1(self):
        print("I am test1!")

    def tearDown(self):#每一个test开头的方法运行完成之后都会执行一次
        print("I am tearDown!")

    @classmethod
    def tearDownClass(cls):#在所有test开头的方法都执行完成之后只执行一次
        print("I am tearDownClass!")

if __name__ == '__main__':
    unittest.main()



 # 运行方式：
# 方法1：nuittest
    # 直接右键或点击绿色小三角以unittest方式运行
    # pass
    # 方法2：no unittest#遗留
    # Sky().test2()

    # 方法3：
    # 方法名必须test开头，否则不会执行。用例执行顺序：根据ASCII码，0~9，A~Z,a~z
    # unittest.main(verbosity=2)  # 三种运行模式，默认verbosity=1；默认执行以test开头的方法。选择unittest模式运行时，可以不加这行，也能执行

    # 方法4：添加多个测试用例。
    # suite = unittest.TestSuite()
    # # suite.addTests([Sky('test2'),Sky('test1'),Sky2('test4'),Sky2('test3')])
    # # suite.addTests([Sky('test2'),Sky('test1')])
    # suite.addTests([Sky1('test2'),Sky1('test1'),Sky2('test4'),Sky2('test3')])
    # runner = unittest.TextTestRunner()
    # runner.run(suite)


    #
    # # 方法5：一次添加一个测试用例。addTest方法后面没有s
    # suite = unittest.TestSuite()
    # suite.addTest(Sky1('test2'))
    # suite.addTest(Sky1('test1'))
    # suite.addTest(Sky2('test3'))
    # suite.addTest(Sky2('test4'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 方法6：模块名.类名，一次添加一个测试文件
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromName('Test1.Sky1'))
    # suite.addTests(unittest.TestLoader().loadTestsFromName('Test2.Sky2'))
    # runner= unittest.TextTestRunner()
    # runner.run(suite)

    # 方法7：模块名.类名，添加多个测试文件，文件里面的方法执行顺序遵循ascii码顺序
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(['Test2.Sky2','Test1.Sky1']))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 方法8：
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky1))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky2))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 方法9：TestResult类的使用方法以及如何查看测试结果
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky1))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky2))
    # result = unittest.TestResult()
    # suite.run(result = result)
    # print('failures', result.failures)#非unittest模式运行才能看到结果
    # print('testsRun', result.testsRun)
    # print('errors', result.errors)

    # 方法10：txt测试报告
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky1))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky2))
    # with open('test_report.txt','w') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)#流
    #     runner.run(suite)

    # 方法11：html测试报告
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky1))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Sky2))
    # with open('test_report.html', 'w') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
    #     runner.run(suite)

