#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 18:15
# @Author  : cui
# @File    : test_liow.py

from jiaoben.ATM.login import Login
from jiaoben.ATM.action.cation_login import Do_login
# 定义必须的方法，完成测试流程的管理
from jiaoben.ATM.test_case.test1 import Test_login


class Flow:
    def main_test(self):
        dr = Login().prepare()
        Test_login().test_login(dr)
        Login().finsh()

