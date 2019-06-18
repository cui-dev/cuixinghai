#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 18:08
# @Author  : xing
# @Site    : 
# @File    : zuiye1.py
# @Software: PyCharm
import HTMLTestRunner
import unittest
import http.client


class login(unittest.TestCase):
    def test1(self):
        parameters = 'username=admin&password=admin&savelogin=true'
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        connect = http.client.HTTPConnection(host='cuishao', port=80)
        connect.request('POST', 'http://cuishao/agileone/index.php/common/login', parameters, head)
        response = connect.getresponse()
        result = response.read().decode('utf8')
        if result == 'successful' and response.status == 200 and response.reason == 'OK':
            print("登录成功！")
        else:
            print("登录失败！")
    def test2(self):

        parameters = 'username=admin&password=admin&savelogin=true'
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        connect = http.client.HTTPConnection(host='cuishao', port=80)
        connect.request('POST', '/agileone/index.php/common/login', parameters, head)
        response = connect.getresponse()
        cookie = response.getheader('Set-Cookie').split(';')[0]
        parameters = 'headline=title103&content=&scope=1&expireddate=2019-08-02'
        head = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': cookie}
        connect = http.client.HTTPConnection(host='cuishao', port=80)
        connect.request('POST', '/agileone/index.php/notice/add', parameters, head)
        response = connect.getresponse()
        result = response.read().decode('utf8')
        self.assertIsNotNone(result, '公告添加失败！')





















"""  
parameters = 'headline=123&content=123&scope=1&expireddate=2019-08-03'
head = {'Content-Type':'application/x-www-form-urlencoded'}
connect = http.client.HTTPConnection(host='cuishao', port=80)
connect.request('POST', 'http://cuishao/agileone/index.php/notice/add', parameters, head)
response = connect.getresponse()

#调用查询接口
parameters = 'currentpage: 1'
head = {'Content-Type': 'application/x-www-form-urlencoded'}
connect1 = http.client.HTTPConnection(host='cuishao', port=80)
connect1.request('POST', 'http://cuishao/agileone/index.php/notice/query', parameters, head)
response = connect1.getresponse()
result = response.read().decode('utf8')
self.assertIn('296',result,'失败')   
"""







suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(login))
with open('test_report.html', 'w') as f:
    runner = HTMLTestRunner.HTMLTestRunner(title='Test Report', stream=f, verbosity=2)
    runner.run(suite)
if __name__ == '__main__':
    unittest.main()

