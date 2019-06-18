import requests

import re
from random import randint
import time
import random
class luwenj:
#     def regiun(self):
#         '''生成身份证前六位'''
#         list1 = []
#         first = randint(1,9)
#         list1.append(first)
#         for i in range(5):
#             first1 = randint(0, 9)
#             list1.append(first1)
#         print(list1)
    def one(self):
        a1=(1985,1,1,0,0,0,0,0,0) #设置开始日期时间元组（1976-01-01 00：00：00）
        a2=(2017,12,31,23,59,59,0,0,0) #设置结束日期时间元组（1990-12-31 23：59：59）
        start=time.mktime(a1)
        #生成开始时间戳
        end=time.mktime(a2)
        #生成结束时间戳 #随机生成10个日期字符串
        for i in range(1):
            t=random.randint(start,end) #在开始和结束时间戳中随机取出一个
            date_touple=time.localtime(t) #将时间戳生成时间元组
            # date=time.strftime("%Y%m%d",date_touple) #将时间元组转成格式化字符串（1976-05-21）
            dates = time.strftime("%Y%m%d",date_touple)
            print(dates)
    def two(self):
        list2 = []
        for i in range(4):
            first = randint(0,9)
            list2.append(first)
        print(list2)

if __name__ == '__main__':
    # luwenj().regiun()
    for i in range(1000):
        luwenj().one()
    # luwenj().two()




















#
# def year():
#     '''生成年份'''
#     # 1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
#     now = time.strftime('%Y')
#     second = random.randint(1948, int(now) - 18)
#     # age = int(now)-second
#     # print('随机生成的身份证人员年龄为：'+str(age))
#     return second
#
#
# def month():
#     '''生成月份'''
#     three = random.randint(1, 12)
#     if three < 10:
#         three = '0' + str(three)
#         return three
#     else:
#         return three
#
#
# def day(year, month):
#     '''生成日期'''
#     four = getDay(year, month)
#     # 日期小于10以下，前面加上0填充
#     if four < 10:
#         four = '0' + str(four)
#         return four
#     return four
#
#
# def getDay(year, month):
#     '''根据传来的年月份返回日期'''
#     # 1，3，5，7，8，10，12月为31天，4，6，9，11为30天，2月闰年为28天，其余为29天
#     aday = 0
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         aday = random.randint(1, 31)
#     elif month in (4, 6, 9, 11):
#         aday = random.randint(1, 30)
#     else:
#         # 即为2月判断是否为闰年
#         if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
#             aday = random.randint(1, 28)
#         else:
#             aday = random.randint(1, 29)
#     return aday
#
#
# def randoms():
#     '''生成身份证后四位'''
#     five = random.randint(1, 9999)
#     if five < 10:
#         five = '000' + str(five)
#     elif 10 < five < 100:
#         five = '00' + str(five)
#     elif 100 < five < 1000:
#         five = '0' + str(five)
#     return five
#
#
# if __name__ == '__main__':







    # # 通过爬取网页获取到身份证前六位
    # url = 'http://www.360doc.com/content/12/0917/16/1888675_236595612.shtml'
    # html = requests.get(url)  # 获取url的网页源码
    # html.encoding = 'UTF-8'
    # soup = BeautifulSoup(html.text, 'lxml')
    # strarr = []
    # for info in soup.find_all(class_='MsoNormal'):
    #     pattern = re.compile(r'\d{6}')
    #     b = re.findall(pattern, info.text)
    #     for item in b:
    #         strarr.append(item)

    # for i in range(1, 50):
    #     # first = regiun(strarr)
    #     second = year()
    #     three = month()
    #     four = day(second, three)
    #     last = randoms()
    #     IDCard = str(first) + str(second) + str(three) + str(four) + str(last)
    #     print('随机生成的身份证号码为：' + IDCard)