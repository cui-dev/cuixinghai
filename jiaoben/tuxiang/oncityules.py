#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 9:30
# @Author  : cui
# @File    : oncityules.py

from appium import webdriver
import os,time


class OneStorkeImge:

    def __init__(self):
        pass

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wb/hub')


    def find_image(self,target):
        base_pash = os.path