#!/usr/bin/env python
#-*- coding:utf-8 -*-

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "4.4.2"
caps["deviceName"] = "127.0.0.1:62001"
caps["noReset"] = True
caps["app"] = "D:\\AndroidSDK\\android-sdk-windows\\build-tools\\28.0.3\\yibijizhang.apk"
caps["appPackage"] = "com.mobivans.onestrokecharge"
caps["appActivity"] = "com.stub.stub01.Stub01"
caps["unicodeKeyboard"] = True#使用unicode编码方式发送字符串
caps["resetKeyboard"] = True#隐藏键盘，此设置执行后手动输入可能无法输入，需要在设置里面恢复下默认输入法


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
sleep(2)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.View")
el1.click()
el2 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/add_txt_In")
el2.click()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")
el3.click()
el4 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/add_et_remark")
el4.click()
el4.send_keys("卖身的")
el5 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_7")
el5.click()
el6 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_0")
el6.click()
el7 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_finish")
el7.click()
result = driver.find_element_by_xpath("//android.widget.TextView[@text='70']").get_attribute('text')

#断言
if result== '70':
    print("牛逼")
else:
    print("垃圾")
driver.quit()