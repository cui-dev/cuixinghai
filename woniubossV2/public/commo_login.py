#!/usr/bin/env python
#-*- coding:utf-8 -*-
#!/usr/bin/env python
#-*- coding:utf-8 -*-
from woniubossV2.browser_driver.browser_driver import Browser_driver
from woniubossV2.read_file.read_txt import Read_txt
import requests

class Common_login:
    def __init__(self):
        self.ip=Read_txt().read_txt()
    #自动化测试登录方法
    def gui_login(self, username):


        dr = Browser_driver().get_driver('chrome')
        url = self.ip + "/WoniuBoss2.0/"
        dr.get(url)
        dr.implicitly_wait(15)
        dr.find_element_by_name("userName").send_keys(username)
        dr.find_element_by_name("userPass").send_keys("woniu123")
        dr.find_element_by_name("checkcode").click()
        dr.find_element_by_name("checkcode").clear()
        dr.find_element_by_name("checkcode").send_keys("0000")
        dr.find_element_by_xpath("//*[text()='登录']").click()
        return dr
    #接口的登录方法
    def api_login(self, username):

        session = requests.session()
        data = {"userName":username,"userPass":"woniu123","checkcode":'0000'}
        resp = session.get(self.ip+"/WoniuBoss2.0/log/userLogin", params=data)
        return session

if __name__ == '__main__':
    Common_login().api_login("WNCD000")