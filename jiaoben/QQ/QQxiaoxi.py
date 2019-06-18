#!/usr/bin/env python
#-*- coding:utf-8 -*-
from time import sleep
import uiautomation
import subprocess#启动程序
class QQ:
    def login(self):
        subprocess.Popen("D:\Tencent\QQ\Bin\QQ.exe")   #启动QQ
        username=uiautomation.WindowControl(Name = "QQ")
        username.ComboBoxControl(Name = "QQ号码").Click()
        username.ComboBoxControl(Name = "QQ号码").SendKeys("1109355448")
        uiautomation.SendKey(uiautomation.Keys.VK_ENTER)   # 按回车键
        self.qun()
        self.quns()

    def qun(self):
        sleep(5)
        password=uiautomation.WindowControl(Name="QQ")  #切换弹窗
        password.TextControl(Name = "联系人").Click()  #单击
        sleep(2)
        password.TextControl(Name = "群聊").Click()
        sleep(2)
        password.ListItemControl(Name = "我的群聊").Click()
        password.ListItemControl(Name="平凡之路").DoubleClick()  #双击
    def quns(self):
        xiaodui = uiautomation.WindowControl(Name="平凡之路")
        xiaodui.EditControl(Name = "输入").Click()
        xiaodui.EditControl(Name = "输入").SendKeys("Hello")
        sleep(3)
        xiaodui.ButtonControl(Name = "发送(&S)").Click()
        one=xiaodui.EditControl(Name="输入").GetWindowText()
        if one is None:
            print("NB")
        else:
            print("LJ")



if __name__ == '__main__':
    QQ().login()