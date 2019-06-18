#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 9:49
# @Author  : cui
# @File    : lianxi1.py
import time
import requests
import hashlib
class login():
    def test1(self):
        ress=requests.session()
        parameters = {"username":"admin","password":"admin","savelogin":"true"}
        ress.post('http://cuishao/agileone/index.php/common/login',parameters)
        parameter = {"headline":"1234567","content":"","scope":"1","expireddate":"2019-08-07"}
        res=ress.post("http://cuishao/agileone/index.php/notice/add",parameter)
        return ress
    def test2(self):
        #文件上传
        ress=self.test1()
        files = {"fileToUpload":open(r"C:\Users\Administrator\Desktop\新建文件夹 (2)\V3\test_case\test_login.py","rb")}
        res=ress.post("http://cuishao/agileone/index.php/attach/upload/refertype/defect/referid/4",files=files)
        print(res.text)
    #MD5加密加密
    def test3(self):
        number=input("输入加密的东西")
        number1=(str(time)+number).encode()
        md5 = hashlib.md5()
        md5.update(number1)
        sign = md5.hexdigest()
        print(sign)

if __name__ == '__main__':
    login().test3()









