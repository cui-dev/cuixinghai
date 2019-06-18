#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 17:56
# @Author  : cui
# @File    : zuoye1.py
import http.client
import unittest
import HTMLTestRunner
import string
class Woniu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('***************开始测试*********************')

    def test2(self):
        #查询接口
        parameters = 'barcode=11111111'
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        connect = http.client.HTTPConnection(host='cuishao', port=8080)
        connect.request('POST', 'http://cuishao:8080/WoniuSales1.4/sell/barcode ', parameters, head)
        response=connect.getresponse()
        #断言
        result = response.read().decode('utf8')
        serial=result.split(',')[7].split(":")[1]
        self.assertIn(serial,result,'垃圾')


    def test3(self):
        parameters = 'barcode='
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        connect = http.client.HTTPConnection(host='cuishao', port=8080)
        connect.request('POST', ' http://cuishao:8080/WoniuSales1.4/sell/barcode  ', parameters, head)
        response = connect.getresponse()
        result = response.read().decode('utf8')
        self.assertNotEqual(result,"[]","error")

    @classmethod
    def tearDownClass(cls):
        print('***************测试结束*********************')


