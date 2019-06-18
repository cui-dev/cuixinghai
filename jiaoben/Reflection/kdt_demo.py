#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os

from jiaoben.Reflection.agileone_test import AgileoneTest


class Kdt:

    def keyword_driven(self):
        agileone = AgileoneTest()
        with open('./data/keyword.txt', 'r') as f:
            reader = csv.reader(f)
            for keywords in reader:
                method_name = keywords.pop(0).lower().replace(' ', '_')
                if hasattr(agileone, method_name):
                    getattr(agileone, method_name)(*keywords)

    def keyword_driven_chinese(self):
        agileone = AgileoneTest()
        keyword_dict = {'打开浏览器': 'open_browser', '输入账号': 'input_text', '输入密码': 'input_password', '登录': 'on_click',
                        '等待': 'wait', '关闭浏览器': 'close_browser'}
        with open('./data/keyword_chinese.txt', 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            for keywords in reader:
                method_name = keyword_dict[keywords.pop(0)]
                if hasattr(agileone, method_name):
                    getattr(agileone, method_name)(*keywords)


if __name__ == '__main__':
    Kdt().keyword_driven_chinese()
