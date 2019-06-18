#! /usr/bin/env python
# -*- coding: utf-8 -*-


def pack_method(*args):
    # 当一个方法的形参前面有一个*号时，表示这是一个装包方法
    # 装包方法的含义就是，我们可以传入无限多的参数，
    # 所传入的所有参数都会被放到一个元组变量中，每一个参数都将是这个元组数据的一个元素。
    # 无论你传入的参数是基本数据类型，还是列表、元组、字典
    # 装包方法常用于设计函数或方法需要不定长参数的场景
    print(type(args), args)


def unpack_method(v1, v2, v3):
    # 对于有参数的函数或方法在调用时，在实参前边加一个*这样的用法叫做拆包方法
    # 拆包方法在运用的时候，你的实参可以是元组，也可以是列表。
    # 但是无论是哪个，一定要注意这个实参的元素个数一定要和被调用的函数或方法的参数个数保持一致，否则就会报错。
    print(type(v1), v1)
    print(type(v2), v2)
    print(type(v3), v3)


def dict_pack_method(**kwargs):
    # 对于形参含有两个*的方法属于字典的装包方法
    # 字典的装包方法，要求传入的参数必须是key=value这样的形式
    # 字典的装包方法也是常用于设计具有不定长参数的函数的方法
    # 假如想设计既有普通的不定长参数又有带键名的不定长参数的函数或方法时怎么写呢，这样写def function(*args, **kwargs)
    print(type(kwargs), kwargs)


def dict_unpack_method(user, age, sex):
    # 对于调用函数或方法时传入一个字典类型的数据，并且这个字典类型的数据前面使用了2个*的情况叫做字典的拆包方法。
    # 字典的拆包方法必须注意的是，传入的字典数据其键名必须和函数或方法的参数个数、名字一一对应。否则就无法拆包成功。
    print(type(user), user)
    print(type(age), age)
    print(type(sex), sex)


if __name__ == '__main__':
    v1 = 'A'
    v2 = 'B'
    v3 = 3
    v4 = ('a', 12, 'c')
    v5 = [1, 2, 3, 'b']
    v6 = [3, 2, 1]
    v7 = ['0', 1]
    print('*********** pack method **************')
    pack_method(v1, v2, v3, v4)
    pack_method(v4)
    pack_method(v5)
    print('*********** unpack method **************')
    # unpack_method(v2, v3, v1)
    # unpack_method(v4[0], v4[1], v4[2])
    unpack_method(*v4)
    unpack_method(*v6)
    # unpack_method(*v5)
    # unpack_method(*v7)
    print('*********** dict pack method **************')
    dict_pack_method(name='张三', age='20', sex='male', grade=11)
    print('*********** dict unpack method **************')
    # dict_unpack_method('李四', 21, 'male')
    dict_data = {'user': '张娜', 'age': 18, 'sex': 'female'}
    dict_unpack_method(**dict_data)
