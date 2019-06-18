#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import time
import random

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Common:

    # 定义一个类级的变量
    driver = None

    # 定义一个获取能够操作界面元素的driver对象的方法
    # 单例模式：我们在获得某一个类的实例话对象的时候，
    # 采用了单例模式设计之后，我们每次获得的这个类的实例化对象本质上都是同一个。
    # 运用单例模式的作用分几方面，一是节约内存资源，
    # 再一个是因为我们的业务场景有时候需要在不同的地方来调用同一个类的实例化对象
    @classmethod
    def get_driver(cls, browser_type='firefox'):
        # 注意这里的cls.driver就等价于Common.driver。
        if cls.driver is None:
            if browser_type == 'firefox' or browser_type == 'ff':
                driver_path = os.path.join(os.getcwd(), 'driver/geckodriver.exe')
                cls.driver = webdriver.Firefox(executable_path=driver_path)
            elif browser_type == 'chrome' or browser_type == 'gc':
                driver_path = os.path.join(os.getcwd(), 'driver/chromedriver.exe')
                cls.driver = webdriver.Chrome(executable_path=driver_path)
            else:
                driver_path = os.path.join(os.getcwd(), 'driver/IEDriverServer.exe')
                cls.driver = webdriver.Ie(executable_path=driver_path)
        cls.driver.set_page_load_timeout(20)
        cls.driver.implicitly_wait(20)
        return cls.driver

    # 定义一个检查元素是否存在的方法
    @classmethod
    def is_element_presence(cls, by, value):
        try:
            # 注意一下find_element方法和以前我们常用的find_element_by_XXX方法的异同之处。
            cls.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    # 定义一个显示等待的方法
    @classmethod
    def wait_for_element_presence(cls, by, value, timeout=10):
        # 第一种显示等待的实现方法
        # for i in range(timeout):
        #     try:
        #         cls.driver.find_element(by, value)
        #         return True
        #     except NoSuchElementException:
        #         time.sleep(1)
        # return False

        # 第二种显示等待的实现方法
        try:
            WebDriverWait(cls.driver, timeout).until(expected_conditions.presence_of_element_located((by, value)))
            # WebDriverWait(cls.driver, timeout).until(lambda dr: dr.find_element(by, value))
            return True
        except TimeoutException:
            return False

    # 定义一个随机等待的方法
    # 注意类方法和静态方法的区别
    # 相同点：
    #       1.静态方法和类方法都是在类里面定义的一个方法
    #       2.静态方法和类方法在调用的时候，都不需要实例化类的对象，直接用类名 + . + 方法名即可使用。
    # 不同点：
    #       1.静态方法、类方法、普通方法他们的第一个参数不同
    #           a. 类方法第一个参数cls，这个等同于类名
    #           b. 普通方法第一个参数self，这个等同于类的实例化对象
    #           c. 静态方法没有类似于上面概念的参数。
    #               注意这个概念不是说静态方法不能有参数，
    #               而是说静态方法没有相当于类方法的类名或普通方法的类的实例化对象性质的参数
    #       2.三者应用场景不同
    #           a. 普通方法应用于要求必须实例化这个类以后，用这个类的实例化对象方可调用本方法的应用场景。
    #           b. 类方法应用于无需实例化这个类，直接用类名来对本方法进行调用的应用场景。
    #           c. 静态方法用于无需实例化这个类，直接用类名来对本方法进行调用，
    #               并且方法体中没有任何东西需要和其所在的类有任何联系的应用场景
    @staticmethod
    def random_sleep():
        time.sleep(random.randint(2, 5))

    # 定义一个浏览器的关闭方法
    @classmethod
    def close_browser(cls):
        cls.driver.quit()
