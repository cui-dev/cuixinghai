#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xlrd


class Read:

    def __init__(self, data_path, sheetname):
        self.data_path = data_path                                 # excle表格路径，需传入绝对路径
        self.sheetname = sheetname                                 # excle表格内sheet名
        self.data = xlrd.open_workbook(self.data_path)             # 打开excel表格
        self.table = self.data.sheet_by_name(self.sheetname)       # 切换到相应sheet
        self.rowNum = self.table.nrows                             # 获取表格行数


    def read_excel(self):
        L=[]
        if self.rowNum < 2:
            print("excle内数据行数小于2")
        else:
            for i in range(1, self.rowNum):#从第二行（数据行）开始取数据
                list = self.table.row_values(i)#获取每一行的数据，返回一个列表

                L.append(list)#将每行数据添加到一个列表中

        return L



if __name__ == '__main__':
    Read('../test_data/test_data.xlsx','登录').read_excel()








