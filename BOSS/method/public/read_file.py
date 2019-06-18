#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xlrd
class Read_File:
    def read_xlsx(self,path):
        excel = xlrd.open_workbook(path)
        # count = len(excel.sheets())
        excel = excel.sheets()[0]
        # print(sheet.nrows)
        # print(sheet.row_values(0))
        # print(sheet)
        # print(count)
        # for sheet in excel.sheets():
        #     print(sheet.text())
        # return sheet
        # table = read_excel('3.xlsx',0)
        list1 = []
        for rownum in range(1, excel.nrows):  # 从第2行读取
            list = excel.row_values(rownum)  # 获取行数据，为列表形式
            # for i in list:
            #     print(i)