#! /usr/bin/env python
# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task
import random


def test_fun1():
    pass


def test_fun2():
    pass


# 1.首先定义一个测试类Agileone，需要继承TaskSet
# 2.在其中定义测试方法，注意添加了@task的才是测试方法
# 3.对于测试方法中我们使用client属性来发送请求，这个属性是与HttpSession类绑定的，也就意味着我们可以调用他的请求方法
# 4.而HttpSession类是requests库的Session类的子类，这也意味着cookie这个东西它会帮助我们管理。
# 5.对于测试前TaskSet类的测试准备以及测试结束的清理我们可以使用on_start和on_stop方法来进行，他们共同的特点都是仅会执行一次。
# 6.在定义好测试类之后，我们需要定义HttpLocust的子类WebSite。
# 7.在这个类中通过task_set来配置测试执行的类，同时也可以配置思考时间
class Agileone(TaskSet):

    # 可以通过tasks参数来指定测试方法执行顺序，并在冒号之后来配置执行的概率。
    # 方法一
    # tasks = {test_fun1: 1, test_fun2: 2}
    # 方法二
    # tasks = [(test_fun1, 1), (test_fun2, 2)]

    def on_start(self):
        self.login_data = {'username': 'admin', 'password': 'admin', 'savelogin': False}

    @task(1)
    def open_homepage(self):
        resp = self.client.get('/agileone/', catch_response=True)
        if 'AgileOne' in resp.text:
            resp.success()
        else:
            resp.failure('open homepage fail.')

    def do_login(self, data):
        return self.client.post('/agileone/index.php/common/login', data=data, catch_response=True)

    @task(2)
    def login(self):
        resp = self.do_login(self.login_data)
        if resp.text == 'successful':
            resp.success()
        else:
            resp.failure('login fail.')

    @task(3)
    def add_notice(self):
        self.do_login(self.login_data)
        data = {'headline': 'this is a notice %d.' % random.randint(1, 1000), 'expireddate': '2019-5-17', 'scope': 1}
        resp = self.client.post('/agileone/index.php/notice/add', data=data, catch_response=True)
        if int(resp.text) > 0:
            resp.success()
        else:
            resp.failure('add notice fail.')


    def on_stop(self):
        print('i am on stop method.')


class Website(HttpLocust):
    task_set = Agileone
    # 下面这两个是设置思考时间
    min_wait = 1000
    max_wait = 2000
    # 设置这个值，我们命令行运行脚本时就不需要添加-H/--host这样的参数了。
    host = 'http://jacky-vpc'

if __name__ == '__main__':
    Website()
