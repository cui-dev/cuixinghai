#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 14:13
# @Author  : cui
# @File    : yidonyunceshi.py

import os,time,threading,subprocess,socket

'''
1.首先通过adb devices 来去查询当前连接了多少台设备
2.依据上边的命令结果提取并获得设备名称列表
3.接下来通过adb -s devices_name shell getprop ro.build version release来查询指定设备的系统版本
4.然后分别构造两个端口，然后检查端口是否被占用，如果占用，那么让端口自增1，直到找到一个没有被占用的端口
5.两个端口分别对应appium启动的时候的-P和-bp两个参数的值
6.端口是否被占用我们需要通过建立socket连接来确定，如果建立的连接都是tcp连接，利用socket的connect/connect_ex方法来检测，前一个方法如果端口没有被占用，他会抛出socket.error类型的错误
后一个方法的端口如果没被占用，他不会抛出错误，他是真正连接上后，方法本身会返回0这个值
7.接下来需要构造并执行appium server的启动命令
8.这个命令是appium -a 127.0.0.1 -p port -bp -port --device-name decice_name --platform-version system_version --log file_path --log-level info --log -timestamp
'''

class MobileCloud:
    #返回设备信息列表，这个列表的每一个元素（devicesName,platformVersion,port,bport)
    def get_devices_info(self):
        devices= subprocess.check_output('adb devices').decode().strip().split('\r\s')  #执行cmd命令，并且返回结果  strip去掉看不见的空格
        list1 = []  #定义一个空列表
        port = 5000  #定义Appium Client 与 Appium Server之间的端口
        bp_port = 8000  #定义Appium Server 与 手机之间的端口
        for i in range(1,len(devices)):
            device_name = devices[i].split('\t')[0].strip()
            platform_version = subprocess.check_output('adb -s %s shell getprop ro.build version selease'%device_name)
            port = self.find_port(port)
            bp_port = self.find_port(bp_port)
            list1.append((device_name,platform_version,port,bp_port))
            port +=1
            bp_port+=1
        return list1

    #检查当前系统可用端口的方法
    def find_port(self,port):
        #这里ckeck_port方法来检查是否被占用，如果以及占用，我们在while循环中让端口号加一
        #然后继续利用此方法检查，直到找到一个没有被占用的端口为止
        while self.check_port(port):
            port +=1
        return port

    def check_port(self,port):
        con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #TCP链接所用
        try:
            con.connect(('127.0.0.1',port))
            con.shutdown(socket.SHUT_RDWR)  #直接关闭
            return True
        except socket.error:
            return False


    #定义方法启动Appium server
    def start_appium(self,device_name,platform_version,port,bp_port):
        log_path = os.path.join(os.getcwd(),'report/%s_appium log'%device_name)  #生成的日志
        #构造cmd命令
        cmd = ''
        #执行命令
        os.system(cmd)


if __name__ == '__main__':
    mc = MobileCloud()
    devices = mc.get_devices_info()  #获得设备列表
    for i in range(len(devices)):
        pass












