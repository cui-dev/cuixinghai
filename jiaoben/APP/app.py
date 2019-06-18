#!/usr/bin/env python
#-*- coding:utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "4.4.2"
caps["deviceName"] = "127.0.0.1:62001"
caps["noReset"] = True
caps["app"] = "D:\\AndroidSDK\\android-sdk-windows\\build-tools\\28.0.3\\xmjsq10.0.12.apk"
caps["appPackage"] = "com.miui.calculator"
caps["appActivity"] = "com.miui.calculator.cal.CalculatorActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.miui.calculator:id/btn_7")
el1.click()
el2 = driver.find_element_by_accessibility_id("加")
el2.click()
el3 = driver.find_element_by_id("com.miui.calculator:id/btn_8")
el3.click()
el4 = driver.find_element_by_xpath("//android.widget.LinearLayout[@content-desc=\"等于\"]/android.view.View")
el4.click()

driver.quit()
