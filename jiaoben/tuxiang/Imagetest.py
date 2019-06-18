#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 16:13
# @Author  : cui
# @File    : Imagetest.py

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import os
import time

# from jiaoben.tuxiang.picture import Imagematch
from jiaoben.tuxiang.OpenCV import   ImageMatchByOpenCV

class ImageTest:

    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.match = ImageMatchByOpenCV()

    def start_app(self, cmd):
        os.system('start /b %s' % cmd)
        time.sleep(5)
        print('start application.')

    def on_click(self, target):
        x, y = self.match.find_image(target)
        self.mouse.click(x, y)
        time.sleep(1)
        print('在[%d, %d]位置单击%s一次。' % (x, y, target))

    def on_double_click(self, target):
        x, y = self.match.find_image(target)
        self.mouse.click(x, y, n=2)
        time.sleep(1)
        print('在[%d, %d]位置双击%s一次。' % (x, y, target))

    def input(self, target, content):
        self.on_double_click(target)
        self.keyboard.type_string(content)
        time.sleep(1)
        print('在%s上输入内容%s。' % (target, content))

    def select(self, target, count=0):
        self.on_click(target)
        for i in range(count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        time.sleep(0.5)
        print('在%s上选择第%d项。' % (target, count + 1))

    def start_test(self):
        self.start_app('java -jar JavaSwingCalc.jar')
        self.input('numberx.png', '200')
        self.input('numbery.png', '100')
        self.select('calctype.png', 1)
        self.on_click('docalc.png')
        time.sleep(2)
        if self.match.check_exist('result.png'):
            print('test success.')
        else:
            print('test fail.')
        self.on_click('doclose.png')


if __name__ == '__main__':
    ImageTest().start_test()
