#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Read_txt:
    def __init__(self):
        self.ip=''
    def read_txt(self):
        with open("../config/IP", "r") as f:
            content=f.read()
            for i in content:
                self.ip+=i
            ip=self.ip.split("=")[1]
        return ip


