# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 17:24
# @Author  : cui
# @File    : boss_job.py
import unittest,time
from woniubossV2.public.commo_login import Common_login
from woniubossV2.public.get_data import Get_data
class Job(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.list1 = Get_data('../test_data/test_gui.xlsx', '就业管理').get_data()
        cls.dr = Common_login().gui_login('WNCD001')
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(15)
        cls.dr.find_element_by_xpath("(//a[@class='list-group-item'])[6]").click()
    def test1(self):
        for i in self.list1:
            if i[-3] == '解密':
                with self.subTest(data=i):
                    self.dr.find_element_by_id("btn-decrypt").click()
                    self.dr.switch_to.alert.send_keys(i[0])
                    self.dr.switch_to.alert.accept()
                    time.sleep(3)
                    if i[4] == '正确':
                        self.dr.refresh()
                        hope=self.dr.find_element_by_xpath("(//td[text()='付文攀'])[1]").text
                        self.assertEqual(hope,i[3],'断言失败')
                    if i[4] == "错误":
                        alert = self.dr.switch_to.alert  # 切换弹窗
                        content = alert.text
                        alert.accept()
                        self.dr.refresh()
                        self.assertEqual(i[3],content,'断言失败')

    def test2(self):
        for i in self.list1:
            if i[-3] == "面试":
                with self.subTest(data=i):
                    self.dr.find_element_by_xpath("(//option[text()='未通过'])[1]").click()
                    self.dr.find_element_by_xpath("(//button[text()='面试'])[1]").click()
                    if i[-1] == "未通过":
                        quiz=self.dr.find_element_by_id("squestion")
                        quiz.click()
                        quiz.send_keys(i[0])
                        evaluate=self.dr.find_element_by_id("sval")
                        evaluate.click()
                        evaluate.send_keys(i[1])
                        self.dr.find_element_by_id("saveSkillbtn").click()
                        alert = self.dr.switch_to.alert  # 切换弹窗
                        content = alert.text
                        alert.accept()
                        self.dr.refresh()
                        self.assertEqual(content,i[-2],"断言失败")
                    # if i[-1] =="通过":
                    #     self.dr.find_element_by_id("isPassSkill").click()
                    #     self.dr.find_element_by_xpath("(//select[@id='isPassSkill'])/option[2]").click()
                    #     quiz = self.dr.find_element_by_id("squestion")
                    #     quiz.click()
                    #     quiz.send_keys(i[0])
                    #     evaluate = self.dr.find_element_by_id("sval")
                    #     evaluate.click()
                    #     evaluate.send_keys(i[1])
                    #     self.dr.find_element_by_id("saveSkillbtn").click()
                    #     try:
                    #         alert = self.dr.switch_to.alert
                    #         mistake=alert.text
                    #         alert.accept()
                    #         self.assertEqual(mistake,i[-2],"断言失败")
                    #         self.dr.refresh()
                    #     except Exception as e:
                    #         raise AssertionError("面试通过没有弹框提示")
                    #     self.dr.refresh()

    def test3(self):
        for i in self.list1:
            if i[-3] == "人数":
                with self.subTest(data=i):
                    if i[-1] == "通过十条":
                        time.sleep(3)
                        target1 = self.dr.find_element_by_xpath("(//a[text()='下一页'])[1]")
                        self.dr.execute_script("arguments[0].scrollIntoView();", target1)
                        time.sleep(1)
                        self.dr.find_element_by_xpath("(//button[@class='btn btn-default dropdown-toggle'])[1]").click()
                        number=self.dr.find_element_by_xpath("(//span[text()='显示第 1 到第 10 条记录，总共 15 条记录'])[1]").text
                        self.assertIn(i[-2],number,"断言失败")
                        self.dr.refresh()
                        time.sleep(3)
                    if i[-1] =="通过十五条":
                        target1 = self.dr.find_element_by_xpath("(//a[text()='下一页'])[1]")
                        self.dr.execute_script("arguments[0].scrollIntoView();", target1)
                        time.sleep(1)
                        self.dr.find_element_by_xpath("(//button[@class='btn btn-default dropdown-toggle'])[1]").click()
                        time.sleep(3)
                        self.dr.find_element_by_xpath('//*[@id="skills"]/div[2]/div[2]/div[4]/div[1]/span[2]/span/ul/li[2]/a').click()
                        number = self.dr.find_element_by_xpath("(//span[text()='显示第 1 到第 15 条记录，总共 15 条记录'])[1]").text
                        self.assertIn(i[-2], number, "断言失败")
                        self.dr.refresh()

    def test4(self):
        for i in self.list1:
            if i[-3] == "翻页":
                with self.subTest(data=i):
                    target1 = self.dr.find_element_by_xpath("(//a[text()='下一页'])[1]")
                    self.dr.execute_script("arguments[0].scrollIntoView();", target1)
                    time.sleep(1)
                    if i[-1] =='下页':
                        self.dr.find_element_by_xpath("(//a[text()='下一页'])[1]").click()
                        time.sleep(3)
                        number=self.dr.find_element_by_xpath("(//span[@class='pagination-info'])[1]").text
                        self.assertIn(i[-2],number,"断言失败")
                        self.dr.refresh()
                    if i[-1] =='上页':
                        self.dr.find_element_by_xpath("(//a[text()='上一页'])[1]").click()
                        time.sleep(3)
                        number = self.dr.find_element_by_xpath("(//span[@class='pagination-info'])[1]").text
                        self.assertIn(i[-2], number, "断言失败")
                        self.dr.refresh()
                    if i[-1] == "跳页":
                        self.dr.find_element_by_xpath("(//a[text()='2'])[1]").click()
                        number = self.dr.find_element_by_xpath("(//span[@class='pagination-info'])[1]").text
                        self.assertIn(i[-2], number, "断言失败")
                        self.dr.refresh()

    def test5(self):
        for i in self.list1:
            if i[-3] == "就业界面":
                with self.subTest(data = i):
                    self.dr.find_element_by_xpath("(//a[text()='就业管理'])[2]").click()
                    if i[-1] == "测试":
                        self.dr.find_element_by_xpath('//select[@id="stu-orientation"]/option[4]').click()
                        hope=self.dr.find_element_by_xpath("(//td[text()='测试'])[1]").text
                        self.assertNotEqual(hope,i[-2],"测试失败")
                        self.dr.refresh()
                    if i[-1] == "开发":
                        self.dr.find_element_by_xpath('//select[@id="stu-orientation"]/option[3]').click()
                        hope = self.dr.find_element_by_xpath("(//td[text()='开发'])[1]").text
                        self.assertNotEqual(hope, i[-2], "测试失败")
                        self.dr.refresh()

    def test6(self):
        for i in self.list1:
            if i[-3] == "就业搜索":
                with self.subTest(data=i):
                    self.dr.find_element_by_xpath("(//a[text()='就业管理'])[2]").click()
                    self.dr.find_element_by_xpath("//input[@class='sel-text']").click()
                    self.dr.find_element_by_xpath("//input[@class='sel-text']").clear()
                    self.dr.find_element_by_xpath("//input[@class='sel-text']").send_keys(i[0])
                    self.dr.find_element_by_xpath("//button[@class='btn btn-padding']").click()
                    if i[-1] == "找到":
                        name = self.dr.find_element_by_xpath("(//td[text()='付文攀'])[2]").text
                        self.assertEqual(name,i[-2],"断言失败")
                        self.dr.refresh()
                    if i[-1] == "找不到":
                        time.sleep(2)
                        hope=self.dr.find_element_by_xpath("//td[@colspan='9']").text
                        self.assertEqual(hope,i[-2],"断言失败")
                        self.dr.refresh()













if __name__ == '__main__':
    unittest.main()