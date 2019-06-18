#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from training.phase11.CBT.ATM.Reporter import Reporter
from training.phase11.CBT.ATM.common import Common


class Login:

    def __init__(self):
        self.driver = Common.get_driver()
        self.report = Reporter('1.0.2')
        self.module = '登录模块'

    # 定义必须的方法，完成测试环境的准备
    def prepare(self):
        self.driver.get('http://jacky-vpc/agileone/')
        if Common.is_element_presence(By.ID, 'username') and 'Welcome' in self.driver.title:
            print('open homepage success.')
        else:
            print('open homepage fail.')

    # 定义必须的方法，完成测试结束的资源清理
    def finish(self):
        Common.close_browser()
        self.report.generate_html()

    # 定义必须的方法，完成测试流程的管理
    def main_test(self):
        self.prepare()
        self.test_login()
        self.finish()

    # 定义一个action组件
    def do_login(self, username, password):
        user = self.driver.find_element_by_id('username')
        user.clear()
        user.send_keys(username)
        psw = self.driver.find_element_by_id('password')
        psw.clear()
        psw.send_keys(password)
        self.driver.find_element_by_id('login').click()
        Common.random_sleep()

    # 定义一个test组件
    def test_login(self):
        user = 'admin'
        psw = 'admin1'
        try:
            self.do_login(user, psw)
            if user in self.driver.find_element_by_id('welcome').text:
                self.report.write_report(self.module, 'UI测试', 'AgileOne_001', '正常登录测试', '成功', '无', '无')
            else:
                self.report.write_report(self.module, 'UI测试', 'AgileOne_001', '正常登录测试', '失败', '登录断言失败', '无')
        except Exception as e:
            screenshot = self.report.capture_screen(self.driver)
            self.report.write_report(self.module, 'UI测试', 'AgileOne_001', '正常登录测试', '错误', str(e), screenshot)
