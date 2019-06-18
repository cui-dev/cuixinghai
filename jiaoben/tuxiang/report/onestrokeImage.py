#! /usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import cv2 as cv
import os
import time


class OneStrokeImage:

    def __init__(self):
        # 初始化appium的相关信息
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.0.2',
            'deviceName': 'Android_5.0',
            'appPackage': 'com.mobivans.onestrokecharge',
            'appActivity': 'com.stub.stub01.Stub01'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 注意因为后面没有使用webdriver的元素定位，所以隐式等待或者显示等待都是无效的，我们需要用sleep强制等待
        time.sleep(10)

    # 定义图片识别方法
    def find_image(self, target):
        base_path = os.path.join(os.getcwd(), 'source')
        screen_path = os.path.join(base_path, 'screen.png')
        # 注意这里使用了appium的截图方法
        self.driver.get_screenshot_as_file(screen_path)
        source = cv.imread(screen_path)
        template = cv.imread(os.path.join(base_path, target))
        # 模板匹配算法
        result = cv.matchTemplate(source, template, cv.TM_CCOEFF_NORMED)
        min, max, min_loc, max_loc = cv.minMaxLoc(result)
        if max > 0.95:
            # 注意一下获得模板宽高的特殊之处
            pos_x = max_loc[0] + int(template.shape[1] / 2)
            pos_y = max_loc[1] + int(template.shape[0] / 2)
            return pos_x, pos_y
        else:
            return -1, -1

    # 定义检查断言方法
    def check_exist(self, target):
        x, y = self.find_image(target)
        return x != -1 and y != -1

    # 定义一个单击的方法
    def on_click(self, target):
        x, y = self.find_image(target)
        if x != -1 and y != -1:
            # 注意tap方法两个参数，
            # 第一个参数要求传入的是一个列表对象，列表的元素应该是一个坐标数据，元组类型对象，
            # 目的是支持移动设备多点触控
            # 第二个参数指的是手指按下的持续时间，单位是毫秒
            self.driver.tap([(x, y)], 10)
            print('在[%d, %d]上单击%s一次。' % (x, y, target))
        else:
            print('没有找到%s对象。' % target)
        time.sleep(1.5)

    def start_test(self):
        self.on_click('new.png')
        self.on_click('type.png')
        self.on_click('number2.png')
        self.on_click('number3.png')
        self.on_click('number8.png')
        self.on_click('done.png')
        time.sleep(1)
        self.on_click('tip.png')
        time.sleep(1)
        if self.check_exist('list.png'):
            print('test success.')
        else:
            print('test fail.')


if __name__ == '__main__':
    OneStrokeImage().start_test()
