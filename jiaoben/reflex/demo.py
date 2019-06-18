#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/6/14 9:52
# software: PyCharm
import random
import sys

class Student:

    def __init__(self):
        self._name = None
        self._age = None
        self._sex = None

    def get_name(self):
        return self._name

    def set_name(self,name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self,age):
        self._age = age

    def get_sex(self):
        return self._sex

    def set_sex(self, sex):
        self._sex = sex

    def get_student(self):
        return 'name: %s,age: %s,sex: %s'%(self._name,self._age,self._sex)

    def set_student(self,name,age,sex):
        self.set_name(name)
        self.set_age(age)
        self.set_sex(sex)


if __name__ == '__main__':
    student = Student()
    student.set_name('lisi')
    print(student.get_name())
    __import__('san.reflex.demo')
    #利用sys来获取模块对象
    module = sys.modules['san.reflex.demo']
    #通过模块对象利
    student_class = getattr(module,'Student')
    stu = student_class()
    stu.set_student('李四',20,'男')
    print(stu.get_student())
    if hasattr(stu,'sex'):
        sex = getattr(stu, 'sex')
        print(sex)
    else:
        print('not dound.')
    if hasattr(stu,'name'):
        #设置属性   利用setattr方法对指定对象的属性赋值
        setattr(stu,'name','赵六')
        print(getattr(stu,'name'))
    if hasattr(stu,'get_name'):
        #利用gettattr方法来获取并执行指定对象的指定方法
        method = getattr(stu,'get_name')
        value = method()
        print(value)
        #简化写法
        print('#'*30)
        print(getattr(stu,'get_name')())
    print('%'*30)
    if hasattr(stu,'set_sex'):
        method_obj = getattr(stu,'set_sex')
        method_obj('女')
        print(getattr(stu,'get_sex')())
        #简化
        getattr(stu,'set_sex')('男')
        print(getattr(stu,'get_sex')())
    print('$'*30 + '反射方法')
    #实例化对象以后全部的方法和属性
    dir_list = stu.__dir__()
    print(dir_list)
    #获取指定类的对象的全部方法和属性名
    dir_list1 = dir(stu)
    #对列表元素名称进行了逆序排序，主要是想把student类中的set方法顺序前置，为了后面教学演示效果而已
    dir_list.sort(reverse = True)
    #对所有方法进行循环处理
    for method_name in dir_list:
        #过滤非自己定义的方法，同时也过滤掉了自己定义的那几个属性
        #利用hasattr方法对满足条件的方法进行了调试
        if not method_name.startswith('_') and hasattr(stu,method_name):
            #获得指定方法名的方法对象
            method = getattr(stu,method_name)
            #对于有参数无参数的方法进行了分别处理
            if method_name.startswith('set'):
                #获得指定方法对象的参数个数，注意减1是为了过滤掉对类的方法定义时的首个参数self的统计
                count = method.__code__.co_argcount - 1
                args = []
                for i in range(count):
                    #利用随机数对所有参数进行了简单的就值
                    args.append(random.randint(1,100))
                #调用并执行有参数的方法
                method(*args)
                print(method_name,args)
            else:
                #调用并执行无参数的方法，同时打印方法的返回值
                print(method_name,method())
