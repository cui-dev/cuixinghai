#!/usr/bin/env python
#-*- coding:utf-8 -*-
class Read:
    def reads(self,filepath):
        list1=[]
        with open(filepath,"r") as f:
            a=f.readlines()
        for i in a:
            list1.append((i[:-1].split("="))[1])
        print(list1)
        return list1
if __name__ == '__main__':
    Read().reads("./1.text")