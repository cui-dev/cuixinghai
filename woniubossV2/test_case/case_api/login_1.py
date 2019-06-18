#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 10:09
# @Author  : cui
# @File    : login_1.py
import requests ,unittest
from woniubossV2.read_file.read_txt import Read_txt
from woniubossV2.public.get_data import Get_data
class Login_port(unittest.TestCase):
    def test4(self):
        ip=Read_txt().read_txt()  #自己的域名加端口
        request=Get_data("../test_data/test_data.xlsx", "登录").get_data()
        for i in request:
            with self.subTest(data=i):
                data={}
                for j in i[0:3]:
                    list1=j.split(":")
                    data[list1[0]]=list1[1]
                url = ip + i[4]
                sess=requests.session()
                session=sess.get(url,params=data)
                if i[6] == "等于":
                    self.assertEqual(session.text,i[5],"断言失败")
                elif i[6] =="包含":
                    self.assertIn(i[5],session.text,"断言失败")


if __name__ == '__main__':
    unittest.main()