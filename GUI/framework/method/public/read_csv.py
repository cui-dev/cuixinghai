#!/usr/bin/env python
#-*- coding:utf-8 -*-
import csv
class Reads:
    def reade(self,path):
        list1=[]
        with open(path) as f:
            number=csv.reader(f)
            for i in number:
                list1.append(i)
        # print(list1)
        return list1

if __name__ == '__main__':
    Reads().reade("../../test_date/datas.csv")