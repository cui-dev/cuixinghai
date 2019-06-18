#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 10:46
# @Author  : cui
# @File    : boss_job1.py
import unittest,time
from woniubossV2.public.commo_login import Common_login
from woniubossV2.public.get_data import Get_data
class Job(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.list1 = Get_data('../test_data/test_gui.xlsx', '就业管理1').get_data()
        cls.dr = Common_login().gui_login('WNCD001')
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(15)
        cls.dr.find_element_by_xpath("(//a[@class='list-group-item'])[6]").click()
        cls.dr.find_element_by_id("btn-decrypt").click()
        cls.dr.switch_to.alert.send_keys("woniu123")
        cls.dr.switch_to.alert.accept()
        cls.dr.refresh()
    def test7(self):
        for i in self.list1:
            if i[-3] == "就业面试":
                with self.subTest(data=i):
                    self.dr.find_element_by_xpath("(//a[text()='就业管理'])[2]").click()
                    self.dr.find_element_by_xpath("(//button[@class='btn btn-info' and @data-toggle='modal'])[1]").click()
                    self.dr.find_element_by_xpath("//a[text()='面试记录']").click()
                    self.dr.find_element_by_xpath("(//span[@class='filter-option pull-left'])[1]").click()
                    self.dr.find_element_by_xpath("(//span[text()='安科思软件（成都）有限公司'])[1]").click()
                    self.dr.find_element_by_xpath("((//select[@class='text'])[3])/option[3]").click()
                    self.dr.find_element_by_id("reatime").send_keys(i[0])
                    self.dr.find_element_by_id("rearemark").send_keys(i[1])
                    self.dr.find_element_by_id("saveEditRBtn").click()
                    if i[-1] == "面试错误":
                        alert = self.dr.switch_to.alert
                        mistake=alert.text
                        alert.accept()
                        self.assertEqual(mistake,i[-2],"断言失败")
                        self.dr.refresh()
                    if i[-1] == "面试正确":
                        self.dr.find_element_by_xpath("(//button[@class='btn btn-info' and @data-toggle='modal'])[1]").click()
                        self.dr.find_element_by_xpath("//a[text()='面试记录']").click()
                        result=self.dr.find_element_by_xpath("//td[@colspan='4']").text
                        self.assertNotEqual(result,i[-2],"断言失败")
                        self.dr.refresh()
                    if i[-1] =="时间错误":
                        try:
                            alert=self.dr.switch_to.alert
                            mistake = alert.text
                            alert.accept()
                            self.assertEqual(i[-1],mistake,"断言失败")
                        except Exception as e:
                            raise AssertionError('时间错误，缺失错误弹窗')
                self.dr.refresh()

    def test8(self):
        for i in self.list1:
            if i[-3] == "模拟面试":
                with self.subTest(data=i):
                    self.dr.find_element_by_xpath("(//a[text()='就业管理'])[2]").click()
                    self.dr.find_element_by_xpath("(//button[@class='btn btn-info' and @data-toggle='modal'])[1]").click()
                    self.dr.find_element_by_xpath("//a[text()='模拟面试']").click()
                    self.dr.find_element_by_id("msalary").send_keys(i[0])
                    self.dr.find_element_by_id("mremark").send_keys(i[1])
                    self.dr.find_element_by_id("saveEditMBtn").click()
                    if i[-1] == "备注为空":
                        try:
                            alert = self.dr.switch_to.alert
                            mistake=alert.text
                            alert.accept()
                            self.assertEqual(mistake,i[-2],"断言失败")
                            self.dr.refresh()
                        except Exception as e:
                            raise AssertionError("添加成功没有弹框提示")
                        self.dr.refresh()


















































if __name__ == '__main__':
    unittest.main()