#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 10:49
# @Author  : cui
# @File    : boss_uploading.py

import unittest,time
from woniubossV2.public.commo_login import Common_login
from woniubossV2.public.get_data import Get_data
class Job(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.list1 = Get_data('../test_data/test_gui.xlsx', '崔').get_data()
        cls.dr = Common_login().gui_login('WNCD000')
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(15)
    # def test1(self):
    #     for i in self.list1:
    #         if i[-3] == "上传文件":
    #             with self.subTest(data = i):
    #                 self.dr.find_element_by_xpath("(//a[@class='list-group-item'])[2]").click()
    #                 if i[1] == 'exl':
    #                     time.sleep(2)
    #                     self.dr.find_element_by_id("files").send_keys(r"D:\PyCharm 2019.1.1\student\woniubossV2\config\boss.xls")
    #                     #上行为上传文件
    #                 if i[1] == "txt":
    #                     time.sleep(2)
    #                     self.dr.find_element_by_id("files").send_keys( r"D:\PyCharm 2019.1.1\student\woniubossV2\config\cui.txt")
    #                     # 上行为上传文件
    #                 self.dr.find_element_by_xpath("//select[@id='regionSelect']/option[2]").click()
    #                 self.dr.find_element_by_xpath("//button[text()='提交']").click()
    #                 alert = self.dr.switch_to.alert
    #                 mistake = alert.text
    #                 alert.accept()
    #                 self.assertEqual(i[-2], mistake, "断言失败")
    #                 self.dr.refresh()






if __name__ == '__main__':
    unittest.main()