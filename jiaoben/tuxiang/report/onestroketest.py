#! /usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import os
import time


class OneStrokeTest:

    def __init__(self, device_name, platform_version, port):
        app_path = os.path.join(os.getcwd(), 'yibijizhang.apk')
        self.device_name = device_name
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': platform_version,
            'deviceName': self.device_name,
            'appPackage': 'com.mobivans.onestrokecharge',
            'appActivity': 'com.stub.stub01.Stub01',
            'app': app_path,
            'unicodeKeyboard': 'True',
            'noReset': 'False'
        }
        self.url = 'http://127.0.0.1:' + str(port) + '/wd/hub'

    def start_test(self):
        self.driver = webdriver.Remote(self.url, self.desired_caps)
        self.driver.implicitly_wait(60)
        try:
            self.driver.find_element_by_android_uiautomator('text("记一笔")').click()
            self.driver.scroll(self.driver.find_element_by_android_uiautomator('text("医疗")'),
                               self.driver.find_element_by_android_uiautomator('text("餐饮")'))
            time.sleep(2)
            self.driver.find_element_by_android_uiautomator('text("书籍")').click()
            editor = self.driver.find_element_by_id('add_et_remark')
            editor.clear()
            editor.send_keys('购买学习资料。')
            self.driver.find_element_by_id('keyb_btn_2').click()
            self.driver.find_element_by_id('keyb_btn_3').click()
            self.driver.find_element_by_id('keyb_btn_8').click()
            self.driver.find_element_by_id('keyb_btn_finish').click()
            self.driver.find_element_by_android_uiautomator('text("长按记录可删除")').click()
            remarks = self.driver.find_elements_by_id('account_item_txt_remark')
            money_list = self.driver.find_elements_by_id('account_item_txt_money')
            if remarks[0].text == '购买学习资料。' and money_list[0].text == '-238':
                print('test success.')
            else:
                print('text fail.')
        except Exception as e:
            with open('./report/%s.log' % self.device_name, 'w') as f:
                f.write(str(e))
            now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            self.driver.get_screenshot_as_file('./report/%s_%s.png' % (self.device_name, now))
        finally:
            self.driver.quit()


if __name__ == '__main__':
    OneStrokeTest().start_test()
