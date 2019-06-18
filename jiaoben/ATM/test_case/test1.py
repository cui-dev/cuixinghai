#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 18:10
# @Author  : cui
# @File    : test1.py

from jiaoben.ATM.action.cation_login import Do_login


class Test_login:

    def test_login(self,dr):
        user = 'admin'
        word = 'admin'
        Do_login().do_login(user, word,dr)
        # 断言方法
        if user in dr.find_element_by_id('welcome').text:
            print('成功')
        else:
            print('失败')