#!/usr/bin/env python
#-*- coding:utf-8 -*-

from selenium import webdriver


class Browser_driver:


    def get_driver(self, browser):
        if browser == "firefox":
            dr = webdriver.Firefox()
        elif browser == "chrome":
            dr = webdriver.Chrome()
        elif browser == "ie":
            dr = webdriver.Ie()
        else:
            dr = webdriver.Firefox()
        return dr


