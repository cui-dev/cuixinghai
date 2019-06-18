#!/usr/bin/env python
#-*- coding:utf-8 -*-
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner_new


# 将测试结果利用HTMLTestRunner第三方库保存成html文件
class RunAllTest:

    def testsuit_api(self):  #接口测试

        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.discover(
            os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))+'\\test_case\\case_api',
         '*.py'))

        with open('../test_report/api_woniuboss_report.html', 'wb') as f:
            runner = HTMLTestRunner_new.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
            runner.run(suite)

    def testsuit_gui(self):#gui测试

        suite = unittest.TestSuite()
        suite.addTests(unittest.defaultTestLoader.discover(
            os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)) + '/test_case/case_gui',
            '*.py'))

        with open('../test_report/gui_woniuboss_report.html', 'wb') as f:
            runner = HTMLTestRunner_new.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
            runner.run(suite)





if __name__ == "__main__":
    r=RunAllTest()
    # r.testsuit_api()
    r.testsuit_gui()