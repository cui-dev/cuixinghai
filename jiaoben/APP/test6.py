#!/usr/bin/env python
#-*- coding:utf-8 -*-
import uiautomator2 as cui
from time import sleep
d = cui.connect("emulator-5554")
sleep(5)
d.press("home")
d(description=u"Apps").click()#打开应用菜单
sleep(1)
d(resourceId="com.android.launcher3:id/icon", text=u"Calculator").click()#打开计算器
sleep(1)
d(className="android.view.ViewGroup", instance=1).click()
d(resourceId="com.android.calculator2:id/op_add").click()
d(resourceId="com.android.calculator2:id/digit_8").click()
d(resourceId="com.android.calculator2:id/eq").click()
d(resourceId="com.android.calculator2:id/digit_9").click()