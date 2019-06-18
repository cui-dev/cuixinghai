#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from time import sleep

from woniubossV2.read_file.read_txt import Read_txt
from woniubossV2.browser_driver.browser_driver import Browser_driver
from woniubossV2.public.get_data import Get_data
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path="../test_data/test_data.xlsx"
        cls.sheetname="登录"
        cls.g=Get_data(cls.path,cls.sheetname)
        cls.ip = Read_txt().read_txt()

    def test_login(self):
        datas_list = self.g.get_data()
        for i in datas_list:
            with self.subTest(data=i):
                dr = Browser_driver().get_driver(i[3])
                url = self.ip+i[4]
                dr.get(url)
                dr.implicitly_wait(15)
                dr.find_element_by_name("userName").send_keys(i[0])
                dr.find_element_by_name("userPass").send_keys(i[1])
                dr.find_element_by_name("checkcode").click()
                dr.find_element_by_name("checkcode").clear()
                dr.find_element_by_name("checkcode").send_keys(i[2])
                dr.find_element_by_xpath("//*[text()='登录']").click()
                result= dr.find_element_by_xpath("//*[text()='注销']").text
                self.assertEqual(i[5], result, '登录失败')
        dr.quit()

if __name__ == '__main__':
    unittest.main()