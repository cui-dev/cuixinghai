#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys


class Student:

    def __init__(self):
        self._name = None
        self._age = None
        self._sex = None

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_sex(self):
        return self._sex

    def set_sex(self, sex):
        self._sex = sex

    def get_student(self):
        return 'name: %s, age: %d, sex: %s' % (self._name, self._age, self._sex)

    def set_student(self, name, age, sex):
        self.set_name(name)
        self.set_age(age)
        self.set_sex(sex)


if __name__ == '__main__':
    student = Student()
    student.set_name('张三')
    print(student.get_name())
    student._age = 25
    print(student._age)
    # 利用反射机制通过模块的字符串名来导入模块
    __import__('training.phase11.CBT.Reflection.student_module')
    # 利用sys来获取模块对象
    module = sys.modules['training.phase11.CBT.Reflection.student_module']
    # 通过模块对象利用getattr方法来获取模块中由传入的字符串参数所指定的类
    student_class = getattr(module, 'Student')
    # 通过类来获取该类的实例化对象
    stu = student_class()
    stu.set_student('李四', 20, '男')
    print(stu.get_student())
    # 利用hasattr方法来查询指定对象中有无要求的属性
    if hasattr(stu, '_sex'):
        # 利用getattr方法来获取对象中的属性值
        sex = getattr(stu, '_sex')
        print(sex)
        print(getattr(stu, '_name'))
    else:
        print('not found.')
    if hasattr(stu, '_name'):
        # 利用setattr方法来对指定对象的指定属性进行赋值
        setattr(stu, '_name', '赵六')
        print(getattr(stu, '_name'))
    print('*************** 无参数的方法调用 ***************')
    if hasattr(stu, 'get_name'):
        # 利用getattr方法来获取并执行指定对象的指定方法
        method_obj = getattr(stu, 'get_name')
        # 对于无参数方法的调用
        value = method_obj()
        print(value)
        # 简化写法
        print(getattr(stu, 'get_name')())
    print('*************** 有参数的方法调用 ***************')
    if hasattr(stu, 'set_sex'):
        # 利用getattr方法来获取并执行指定对象的指定方法
        method_obj = getattr(stu, 'set_sex')
        # 对于有参数方法的调用
        method_obj('女')
        print(getattr(stu, 'get_sex')())
        # 简化写法
        getattr(stu, 'set_sex')('女')
        print(getattr(stu, 'get_sex')())
    print('*************** 反射方法 ***************')
    # dir_list = stu.__dir__()
    # 获取指定的类的对象的全部方法和属性名
    dir_list = dir(stu)
    print(dir_list)
    # 对列表元素按名称进行了逆序排序，主要是想把student类中的set方法顺序前置，为了后面教学演示效果而已
    dir_list.sort(reverse=True)
    # 对所有方法进行循环处理
    for method_name in dir_list:
        # 过滤非自己定义的方法，同时也过滤掉了自己定义的那几个属性
        # 利用hasattr方法对满足条件的方法名进行了测试
        if (not method_name.startswith('_')) and hasattr(stu, method_name):
            # 获得指定方法名的方法对象
            method = getattr(stu, method_name)
            # 对于有参数的方法和无参数的方法进行了分别处理
            if method_name.startswith('set'):
                # 获取指定方法对象的参数个数，注意减1是为了过滤掉对类的方法定义时的首个参数self的统计
                count = method.__code__.co_argcount - 1
                args = []
                for i in range(count):
                    # 利用随机数对所有参数进行了简单的赋值
                    args.append(random.randint(1, 100))
                # 调用并执行有参数的方法
                method(*args)
                print(method_name, args)
            else:
                # 调用并执行无参数的方法，同时打印方法的返回值。
                print(method_name, method())
