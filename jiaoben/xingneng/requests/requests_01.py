#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 12:17
# @Author  : cui
# @File    : requests_01.py
from parameterized import parameterized
import requests
import unittest


class Woniu_Sales(unittest.TestCase):
    @parameterized.expand([
        ('shell_1','admin', 'admin', '0000','login-pass')
    ])
    def test1(self,id,user,word,code,hope):
        sessions = requests.session()
        url = 'http://cuishao:8080'
        parametes = {'username': user, 'password': word, 'verifycode': code}
        resp = sessions.post('%s/WoniuSales1.4/user/login'%url, parametes)
        self.assertEqual(resp.text, hope, '登陆失败！')
