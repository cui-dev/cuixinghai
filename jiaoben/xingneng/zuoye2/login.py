#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/6 20:52
# @Author  : cui
# @File    : login.py
import http.client
import unittest
class Wonius(unittest.TestCase):


    def test1(self):
        #登陆接口
        parameters = 'username=admin&password=admin&verifycode=0000'
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        connect = http.client.HTTPConnection(host='cuishao', port=8080)
        connect.request('POST', 'http://cuishao:8080/WoniuSales1.4/user/login ', parameters, head)
        connect.getresponse()