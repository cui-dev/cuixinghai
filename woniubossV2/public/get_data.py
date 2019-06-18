#!/usr/bin/env python
#-*- coding:utf-8 -*-

from woniubossV2.read_file.read_file import Read

class Get_data:
    #调用获取数据的类需要手动修改对应的表名和路径
    def __init__(self,data_path, sheetname):
        self.data_path=data_path
        self.sheetname=sheetname
        self.get_datas = Read(self.data_path,self.sheetname)
        self.rowNum = self.get_datas.rowNum

    def datas(self, testdata):
        list1=testdata.split('\n')
        test = []
        for i in list1:
            td = i.split('=')[1]
            test.append(td)
        return test
    def get_data(self ):
        list2=[]
        sheetList = self.get_datas.read_excel()
        for index in range(0, len(sheetList)):
            datas = []
            if index<=len(sheetList):
                browser = sheetList[index][0]
                url = sheetList[index][1]
                test_num=sheetList[index][2]
                test_data = sheetList[index][3]
                test=self.datas(test_data)
                for i in test:
                    datas.append(i)
                hope = sheetList[index][4]
                index+=1
                datas.append(browser)
                datas.append(url)
                datas.append(hope)
                datas.append(test_num)
                list2.append(datas)
            else:
                pass
        return list2

if __name__ == '__main__':
    Get_data("../test_data/test_gui.xlsx", "登录").get_data()
