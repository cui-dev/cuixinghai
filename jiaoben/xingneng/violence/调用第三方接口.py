#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 16:57
# @Author  : cui
# @File    : 调用第三方接口.py
# http://www.webxml.com.cn/zh_cn/web_services.aspx
#WebService相当于http+xml
# '''
# 手机号码归属地查询
import requests
a=input()
url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'
param = {'mobileCode':a,'userID':''}
resp = requests.post(url,param)
content = resp.text
print(content)
# if '陕西 西安 陕西联通GSM卡' in content:
#     print("测试成功！")
# else:
#     print("测试失败！")a
#城市天气
# import requests
# while 1:
#     a=input("请输入你要查询的城市天气")
#     url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather'
#     param = {'theCityCode':a,'theUserID':''}
#     resp = requests.post(url,param)
#     print(resp.text)
#     b=input("继续嘛1.继续2.退出")
#     if b == "1":
#         pass
#     elif b =="2":
#         exit("拜拜")

#IP地址查询
# import requests
# url = 'http://ws.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx/getCountryCityByIp'
# param = {'theIpAddress':'1.5.3.4'}
# resp = requests.post(url,param)
# print(resp.text)


#中英文双向翻译
# import requests
# url = 'https://fanyi.baidu.com/langdetect'
# while 1 :
#     word=input("请输入你要查的单词")
#     param = {'query': word}
#     resp = requests.post(url,param).text
#     print(resp)
#     number=input(" 需要继续嘛,1.继续。2.退出")
#     if number == '1':
#         pass
#     else:
#         exit("拜拜")

# import requests
# herder = {"Upgrade-Insecure-Requests": "1",
#           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
#           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#           "Accept - Encoding": "gzip, deflate, br"}
# url = 'https://www.oschina.net/'
# resp = requests.get(url,verify = False,headers = herder)
# resp.encoding="utf8"
# print(resp.text)















# import requests
# url = ' http://ws.webxml.com.cn/WebServices/ValidateCodeWebService.asmx/smallValidateImage'
# verification=input("请输入你的验证码")
# param = {'byString':verification}
# resp = requests.post(url,param)
# resps=resp.text
# with open('home1.jpg','wb') as f:
#     f.write(resp.content)