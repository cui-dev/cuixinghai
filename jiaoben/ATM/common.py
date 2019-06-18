#!/usr/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 9:41
# @Author  : cui
# @File    : common.py

from selenium import webdriver
import os,time,random

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Common:

    #定义一个类级的变量
    driver = None

    #定义能够操作界面元素的driver对象
    #单例模式:我们在获得某一个类实例化对象的时候，采用单例模式，每次获得的这个类的实例化对象本质上都是同一个
    #运用单例模式作用1.节约内存资源；2.业务场景有时候需要在不同的地方来调动同一个类的实例化对象
    #@classmethod定义类方法
    @classmethod
    def get_driver(cls,browser_type = 'firefox'):
        #cls.driver就等于Common.driver
        if cls.driver is None:
            if browser_type == 'firefox' or browser_type == 'ff':
                driver_path = os.path.join(os.getcwd(),'driver\geckodriver.exe')
                cls.driver = webdriver.Firefox(executable_path=driver_path)   #生产火狐的浏览器对象
            elif browser_type == 'chrome' or browser_type == 'gc':
                driver_path= os.path.join(os.getcwd(),'driver\chromedriver.exe')  #谷歌
                cls.driver = webdriver.Chrome(executable_path=driver_path)
            else:
                driver_path = os.path.join(os.getcwd(), 'driver\IEDriverServer.exe') #IE
                cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.set_page_load_timeout(20)
        cls.driver.implicitly_wait(20)
        return cls.driver


    #检查元素是否存在
    #by:元素定位方式。比如Id value:定位的元素
    @classmethod
    def is_element_presence(cls,by,value):
        try:
            #注意此处的find_element方法和常用的find_element_by_XXX方法的异同之处
            cls.driver.find_element(by,value)
            return True
        except NoSuchElementException:
            return False


    @classmethod
    #timeout  超时的时间,可进行自定义
    #显示等待的方法
    def wait_for_element_presence(cls,by,value,timeout):
        # for i in range(timeout):
        #     try:
        #         cls.driver.find_element(by,value)
        #         return True
        #     except NoSuchElementException:
        #         time.sleep(1)
        # return False

    #第二种显示等待的方法
        try:
            WebDriverWait(cls.driver,timeout).until(expected_conditions.presence_of_element_located((by,value)))
            # WebDriverWait(cls.driver,timeout).until(lambda dr:dr.find_element(by,value))#二者选一即可
            return True
        except TimeoutException:
            return False

    #静态方法，随机等待的方法
    @staticmethod
    def random_sleep():
        #min最小等待时间
        #最大等待时间
        time.sleep(random.randint(2,5))

    @classmethod
    def close_browser(cls):
        cls.driver.quit()

'''
注意类方法和静态方法的区别
#相同点:
    1.静态方法和类方法都是在类里边定义的一个方法
    2.调用方法时，都不需要实例化类，直接用类名+ . + 方法即可使用
    
#区别
    1.静态方法、类方法、普通方法第一个参数不同
        类方法第一个参数cls这个等同于类名
        普通方法第一个参数self ，这个等同于类的实例化对象
        静态方法没有类似于上面概念的参数，不是说静态方法没有参数，是没有相当于类方法的类名或普通方法的类的实例化对象性质的参数
    2.应用不同
        普通方法应用与要求必须实例化这个类以后，用这个类的实例化对象方法可调用本方法的应用
        类方法无需实例化这个类，直接类名来对本方法进行调用的应用场景
        静态方法无需实例化类，直接用类名对本方法进行调用，并且方法体中的参数跟其他方法没有任何关系
'''


