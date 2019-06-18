#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 20:16
# @Author  : cui
# @File    : bss_job2.py

import requests ,unittest,json
from woniubossV2.read_file.read_txt import Read_txt
from woniubossV2.public.get_data import Get_data
from woniubossV2.public.commo_login import Common_login
class Boss_ports(unittest.TestCase):
    def test3(self):
        ip = Read_txt().read_txt()  # 自己的域名加端口
        request = Get_data("../test_data/test_data.xlsx", "显示人数").get_data()
        session = Common_login().api_login('WNCD001')
        for i in request:
            if i[2] == "显示人数":
                with self.subTest(data=i):
                    data = {}
                    for j in i[0:2]:
                        list1=j.split(":")
                        data[list1[0].strip()]=list1[1].strip()
                    url = ip+i[3]
                    sesson=session.post(url,data=data)
                    sess= sesson.text
                    jsons=json.loads(sess)
                    self.assertEqual(i[4],jsons['pageSize'],"断言失败")
