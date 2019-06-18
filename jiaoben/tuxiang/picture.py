#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 14:12
# @Author  : cui
# @File    : picture.py

from PIL import Image,ImageGrab
import os

#1.定义图像匹配算法类ImageMatch
#2.初始化，定义截屏screen,模板tempiate图片的变量，还要定义screen_data,template_data图片像素数据的变量
#3.定义像素的比较方法compare，传入参数分别是要比较的两个像素点，每个像素点实际上是一个元组数据，返回的结果是一个布尔值
#4.定义查找图像识别算法的核心部分，完成模板匹配的功能方法find_image.传入参数为模板图片，返回值为中心点坐标，如果没找到，那么返回-1，-1这样的坐标。
#5.针对fing_image方法，首先获取当前眼测试系统的被测画面（大屏幕），利用Image的Open方法，打开模板图片
#6.得到的图片对象的size属性，分别获取大小图画面的宽高尺寸，在利用得到图片的load方法来获取大小图的像素数据
#7.定义返回的位置变量pos_x,pos_y，分别给她两赋除值-1，-1.
#8.利用双层嵌套循环，模拟滑动匹配的过程，其中外层循环应该是y轴，内层循环代表x轴，循环的范围是0~screen_width-template-width,高度也类似
#9.循环体中，首先利用分支语句进行判断，如果5个特征点均匹配，那么执行全像素匹配的过程，否则，执行下一个循环，对下一个位置进行比对
#10.如果全像素匹配不成功，则继续下一个循环，如果匹配成功，那么依据当前的x,y值以及模板图片的宽高计算中心点坐标
#11.对于全像素匹配，把他单独定义为一个方法check_match,传入参数应该就是我们当前的大图上的左定点坐标，返回的结果是一个布尔值
#12.在check_match方法中重新获取模板图片的宽高数据，然后再次利用嵌套的双层循环来进行全像素匹配，注意这时我们的条件分支去检查像素点不匹配的情况，只要遇到一个点不匹配，说明全像素匹配失败
#13.最够定义一个进行图像识别时候的断言方法check_exist.传入参数就是要查找的图片，返回值是布尔值
#14.直接调用刚才实现的find_image的方法，然后检查返回值，如果坐标是-1，-1，代表没找到图片，返回False;否则，返回True
class Imagematch:

    def __init__(self):
        self.screen = None #定义大图对象
        self.template = None #定义小图对象
        self.screen_data = None #定义大图的像素点数据对象
        self.template_data = None #定义小图的像素点数据对象

    def compare(self,p1,p2):
        #定义像素比较方法，p1和p2就代表要比较的像素点，他们都是元组类型的数据
        return p1[0] == p2[0] and p1[1] == p2[1] and p1[2] == p2[2] and p1[3] == p2[3]

    def find_image(self,target):
        base_path = os.path.join(os.getcwd(),"source")
        # 获取大图小图的对象
        self.screen = ImageGrab.grab().convert('RGBA')
        self.template=Image.open(os.path.join(base_path,target)).conver('RGBA')
        #获取大图和小图的宽高数据
        screen_width,screen_height=self.screen.size
        template_width,template_height=self.template.size
        #获取大图和小图的像素数据
        self.screen_data = self.screen.load()
        self.template_data=self.template.load()
        #定义返回的位置变量，并赋值-1，-1
        pos_x,pos_y=-1,-1
        #利用双层循环来模拟实现滑动比对的过程
        for y in range(screen_height-template_height):
            for x in range(screen_width-template_width):
                #进行条件判断，检查5个特征点，如果匹配就进行全像素比对
                #依次为左顶点，右顶点，左下角，右下角，中心点
                if self.compare(self.screen_data[x,y],self.template_data[0,0]) and\
                    self.compare(self.screen_data[x+template_width-1,y],self.template_data[template_width-1,0]) and\
                    self.compare(self.screen_data[x,y+template_height-1],self.template_data[0,template_height-1])  and \
                    self.compare(self.screen_data[x+template_width-1,y+template_height-1],self.template_data[template_width-1,template_height-1]) and\
                    self.compare(self.screen_data[x+int(template_width/2),y+int(template_height/2)],self.template_data[int(template_width/2),int(template_height/2)]):
                    is_match = self.check_match(x,y)
                    if is_match:
                    #全像素匹配成功就计算中心点坐标并返回
                        pos_x=x+int(template_width/2)
                        pos_y=y+int(template_height/2)
                        return pos_x,pos_y

            return pos_x,pos_y
        #定义一个全像素匹配方法
    def check_match(self,x,y):
        template_width,template_height = self.template.size
        for small_y in range(template_height):
            for small_x in range(template_width):
                if not self.compare(self.screen_data[x+small_x],self.template_data[y+small_y]):
                    return False
        return True

    # 定义一个全像素匹配方法，加入容错处理
    def check_match_similarity(self,x,y,similarity=1.0):
        template_width, template_height = self.template.size
        total_count=template_width*template_height
        unmatch_count = 0
        for small_y in range(template_height):
            for small_x in range(template_width):
                if not self.compare(self.screen_data[x + small_x], self.template_data[y + small_y]):
                    unmatch_count+=1
        return unmatch_count /total_count <= 1- similarity


    #定义一个检查方法
    def check_exist(self,target):
        x,y = self.find_image(target)
        return x != -1 and y != -1

























