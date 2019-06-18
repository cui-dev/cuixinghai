#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 14:54
# @Author  : cui
# @File    : boss_job.py
import requests ,unittest,json
from woniubossV2.read_file.read_txt import Read_txt
from woniubossV2.public.get_data import Get_data
from woniubossV2.public.commo_login import Common_login
class Login_ports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ip = Read_txt().read_txt()  # 自己的域名加端口
        cls.request = Get_data("../test_data/test_data.xlsx", "就业管理").get_data()
        cls.session = Common_login().api_login('WNCD001')
    def test1(self):
        for i in self.request:
            if i[4] == "提交按钮":
                with self.subTest(data=i):
                    data={}
                    for j in i[0:4]:
                        list1=j.split(":")
                        data[list1[0]]=list1[1]
                    url = self.ip + i[5]
                    sess=self.session.post(url,params=data)
                    if i[7] == "等于":
                        self.assertEqual(sess.text,i[6],"断言失败")
                    elif i[7] =="状态码":
                        self.assertIn(i[6],sess.text,"断言失败")
                        # self.assertEqual(number, int(i[6]), "断言失败")
    def test2(self):
        for i in self.request:
            if i[6] == "搜索":
                with self.subTest(data=i):
                    data = {}
                    for j in i[0:6]:
                        list1=j.split(":")
                        data[list1[0].strip()]=list1[1].strip()
                    url = self.ip + i[7]
                    sesson=self.session.post(url,data=data)
                    sess=sesson.text
                    jsons=json.loads(sess)
                    self.assertEqual(int(i[8]),jsons['totalRow'],"断言失败")




















if __name__ == '__main__':
    unittest.main()
