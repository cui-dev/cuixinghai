#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:30
# @Author  : cui
# @File    : OpenCV.py
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import ImageGrab
import cv2 as cv
import os
import time


class ImageMatchByOpenCV:

    def find_image(self, target):
        base_path = os.path.join(os.getcwd(), 'source')
        # 定义截取屏幕图片的保存位置
        screen_path = os.path.join(base_path, 'screen.png')
        # 截取屏幕图片并保存到文件
        ImageGrab.grab().save(screen_path)
        # 利用opencv的imread方法来获取大图和小图的图片对象
        screen = cv.imread(screen_path)
        template = cv.imread(os.path.join(base_path, target))
        # 利用opencv的matchTemplate方法来进行模板匹配
        result = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)
        # 获取匹配的结果
        min, max, min_loc, max_loc = cv.minMaxLoc(result)
        # 依据获得的左顶点的位置来计算中心点的坐标。
        # 注意获取模板图片宽度和高度的方法，利用template对象的shape属性来获取，
        # 但是需要强调的是这个属性得到的结果是一个元组，并且这个元组数据表示的是高、宽含义，
        # 注意顺序与别的地方宽、高不同。
        pos_x = max_loc[0] + int(template.shape[1] / 2)
        pos_y = max_loc[1] + int(template.shape[0] / 2)
        similarity = max
        if similarity > 0.95:
            return pos_x, pos_y
        else:
            return -1, -1


    def check_exist(self, target):
        x, y = self.find_image(target)
        return x != -1 and y != -1


    def check_exist(self, target):
        x, y = self.find_image(target)
        return x != -1 and y != -1
