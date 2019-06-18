#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 18:25
# @Author  : cui
# @File    : requests_02.py
from parameterized import parameterized
import requests
import unittest
import json
class market_inquire(unittest.TestCase):
    @parameterized.expand([
        ('shell_3','1234567890123456789012345678901','[]'),
        ('shell_4','','[]'),
        ('shell_5','衣服','[]'),
        ('shell_6','%@#','[]'),
        ('shell_7','asdfghjkl','[]')
    ])
    def test2(self,id,number,hope):
        sessions = requests.session()
        url = 'http://cuishao:8080'
        parametes = {'barcode':number}
        resp = sessions.post('%s/WoniuSales1.4/sell/barcode' %url, parametes).text
        self.assertEqual(resp, hope, '查询失败！')

    @parameterized.expand([
        ('shell_2','1234','1234')
    ])
    def test3(self,id,number,hope):
        sessions = requests.session()
        url = 'http://cuishao:8080'
        parametes = {'barcode':number}
        resp = sessions.post('%s/WoniuSales1.4/sell/barcode' %url, parametes).text
        resps=json.loads(resp)[0]['barcode']
        self.assertEqual(resps, hope, '查询失败！')

if __name__ == '__main__':
    unittest.main()