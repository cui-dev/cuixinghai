#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 15:11
# @Author  : cui
# @File    : Report.py

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pymysql
import os
import time
import zipfile


# 定义一个测试报告类
# 在设计这个测试报告类之前，我们需要先手工安装pymysql这样一个第三方库
class Reporter:

    # 定义通过指定的版本来构造一个测试报告的实例化类的对象
    def __init__(self, version):
        self.version = version

    # 定义一个保存测试数据到数据库的方法
    # 1. 首先需要利用pymysql的connect方法来连接数据库从而获得数据库连接对象conn。
    # 2. 接下来需要通过conn对象来获取一个游标对象。
    # 3. 拼凑我们的sql插入数据的指令。
    # 4. 利用游标对象的execute方法来执行上面的sql指令。
    # 5. 接下来还需要执行游标对象的commit方法才能够真正改变数据库中的结果。
    # 6. 最后我们就剩下清理资源的活了，先关闭游标，然后再关闭数据库连接。
    def write_report(self, module, testtype, caseid, casetitle, result, error, screenshot):
        conn = pymysql.connect(user='root', passwd='root',
                               host='jacky-vpc', db='woniucbt', charset='utf8')
        cursor = conn.cursor()
        testtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        sql = "insert into report(version, module, testtype, caseid, casetitle, result, testtime, error, screenshot)" \
              " values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"\
              % (self.version, module, testtype, caseid, casetitle, result, testtime, error, screenshot)
        print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    # 获取时间的方法
    def get_time(self):
        now = time.localtime(time.time())
        current_date = time.strftime("%Y%m%d", now)
        current_time = time.strftime("%Y%m%d_%H%M%S", now)
        return current_date, current_time

    # 获取测试报告的生成目录
    def get_report_folder(self, c_date=None):
        if c_date is None:
            c_date = ''
        report_folder = os.path.abspath('.') + '\\report\\report%s_%s' % (c_date, self.version)
        if not os.path.exists(report_folder):
            os.makedirs(report_folder)
        return report_folder

    # 定义一个捕获现场图片的方法
    def capture_screen(self, driver):
        c_date, c_time = self.get_time()
        report_folder = self.get_report_folder(c_date)
        screenshot_folder = os.path.join(report_folder, 'screenshot')
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)
        screenshot = os.path.join(screenshot_folder, c_time + '.png')
        driver.get_screenshot_as_file(screenshot)
        # 注意返回结果实质是截图的相对路径，但因为/这个字符无法直接写入数据库，所以我们使用-字符来代替。
        return "screenshot-" + c_time + ".png"




# 定义一个从数据库中读取当前指定版本数据并输出html
# 1.首先利用pymsql的connect方法来获取一个数据库链接对象
# 2.利用conn对像获取游标对像
# 3.拼凑SQL指令用来查询数据库中是否已有当前版本的测试数据select * from repott(表名) where version = 'vesion-value'
# 4.通过游标对像的execute方法来执行sql指令
# 5.通过游标对像fetchall方法来获取查询结果集
# 6.对保存有结果集的列表对像进行长度检查，长度为0意味着没找到测试数据，那么直接返回，不用生成报告
# 7.如果检测发现长度不为0,那说明需要生成报告，那么继续
# 8.接下来读取测试报告模板文件，把得到的内容字符串保存在一个变量content中
# 9.先通过结果集的第0个记录的第一个字段来获取当前版本
# 10.然后利用字符串中的replace方法替换content中的$test_version
# 11.继续构造sql指令，主要分别去构造统计统计成功，失败，错误的指令，然后分别去执行sql指令
# 12.对于执行结果获取数据时通过游标对像调用fetchone方法获取第0个元素就是我们想要统计结果
# 13.然后利用字符串中的replace方法替换content中的$pass-count,$fil-count,$error-count
# 14.继续构造sql指令来获取测试数据最新一条记录的时间，利用降序排序，取第一条
# 15.执行sql并利用fetchone方法获取结果，最后利用字符串替换方法对content的$last-time和$test-data进行数据更新
# 16.依据结果集results的数量构造循环并且拼接测试结果内容条目的heml代码
# 17.拼好之后利用字符串替换方法对content的$test-result进行数据更新
# 18.准备要保存的测试报告路径，然后利用open方法放入w模式将content的数据写入最终的测试报告文件即可


#定义生成报告的方法
    def generate_html(self):
        conn = pymysql.connect(user='root', passwd='root', host='jacky-vpc', db='woniucbt', charset='utf8')
        cursor = conn.cursor()
        # 查询指定版本的测试数据
        sql = "select * from report where version = '%s'" % self.version
        cursor.execute(sql)
        # 获取查询的结果集，注意fetchall方法的使用
        results = cursor.fetchall()
        if len(results) == 0:
            # 当没找到测试数据时就不生成测试报告
            return
        # 打开并读取测试报告
        tempate_path = os.path.abspath('.') + '\\report\\template.html'
        tempate = open(tempate_path, mode='r', encoding='UTF-8')
        content = tempate.read()
        version = results[0][1]
        # 替换模板中的测试版本为真实数据
        content = content.replace("$test-version", version)
        # 构造测试结果统计数据的sql指令
        sql_base = "select count(*) from report where version='%s' and " % version
        sql_pass = sql_base + "result='成功'"
        cursor.execute(sql_pass)
        # 注意fetchone方法的使用
        pass_count = cursor.fetchone()[0]
        content = content.replace("$pass-count", str(pass_count))
        sql_fail = sql_base + "result='失败'"
        cursor.execute(sql_fail)
        fail_count = cursor.fetchone()[0]
        content = content.replace("$fail-count", str(fail_count))
        sql_error = sql_base + "result='错误'"
        cursor.execute(sql_error)
        error_count = cursor.fetchone()[0]
        content = content.replace("$error-count", str(error_count))
        # 获取最后一条测试数据的测试时间
        sql_last = "select testtime from report where version='%s' order by id desc limit 0,1" % version
        cursor.execute(sql_last)
        last_time = cursor.fetchone()[0]
        content = content.replace("$last-time", str(last_time))
        content = content.replace("$test-date", str(last_time))
        test_result = ""
        # 开始拼接测试数据内容的html代码
        for record in results:
            test_result += "<tr height='40'>"
            test_result += "<td width='7%'>" + str(record[0]) + "</td>"
            test_result += "<td width='9%'>" + record[2] + "</a></td>"
            test_result += "<td width='9%'>" + record[3] + "</td>"
            test_result += "<td width='7%'>" + record[4] + "</td>"
            test_result += "<td width='20%'>" + record[5] + "</td>"
            if record[6] == '成功':
                test_result += "<td width='7%' bgcolor='lightgreen'>" + record[6] + "</td>"
            elif record[6] == '失败':
                test_result += "<td width='7%' bgcolor='red'>" + record[6] + "</td>"
            elif record[6] == '错误':
                test_result += "<td width='7%' bgcolor='yellow'>" + record[6] + "</td>"
            test_result += "<td width='16%'>" + str(record[7]) + "</td>"
            test_result += "<td width='15%'>" + record[8] + "</td>"
            screenshort = record[9].replace('-', '/')
            if screenshort == '无':
                test_result += "<td width='10%'>" + screenshort + "</td>"
            else:
                test_result += "<td width='10%'><a href='" + screenshort + "'>查看截图</a></td>"
            test_result += "</tr>\r\n"
        content = content.replace("$test-result", test_result)
        # 拼凑测试报告生成路径
        c_date, c_time = self.get_time()
        report_folder = self.get_report_folder(c_date)
        report_path = os.path.join(report_folder, c_time + '_cbt.html')
        # 将content保存到指定的测试报告文件中
        report = open(report_path, mode='w', encoding='utf8')
        report.write(content)
        # 清理资源
        tempate.close()
        report.close()
        cursor.close()
        conn.close()

    # 定义一个压缩测试报告文件的方法
    def compress_report(self):
        filelist=[]
        c_date, c_time = self.get_time()
        report_folder = self.get_report_folder(c_date)
        print('report_folder:', report_folder)
        root_folder = os.path.split(report_folder)[1]
        print('root_folder:', root_folder)
        # 构造压缩文件的路径
        zipfilename = 'report\\report_' + c_time + '.zip'
        # 压缩文件的方法，获得压缩文件对象
        zip = zipfile.ZipFile(zipfilename, 'w', zipfile.ZIP_LZMA)
        # 查找并获取要进行压缩的文件，利用os模块提供的walk方法来遍历文件夹
        for root, folders, filenames in os.walk(report_folder):
            for folder in folders:
                filelist.append(os.path.join(root, folder))
            for filename in filenames:
                if 'Thumbs.db' not in filename:
                    filelist.append(os.path.join(root, filename))
        for file in filelist:
            print('file：', file)
            # zip压缩文件写入方法有两个参数，
            # 第一个参数用来指定要压缩的文件路径，
            # 第二个参数的名字叫做锚位置。若不指定锚位置，那么压缩文件将保存文件的全路径，
            # 若指定了锚位置，那么压缩文件将以该路径为根路径来进行保存
            zip.write(file, file.split(root_folder)[1])
        zip.close()
        return zipfilename

    # 定义一个自动发送邮件的方法
    # def send_mail(self, attachment):
class Mail:
    def send_mail(self):
        # 定义一个发件人
        sender = '1109355448@qq.com'
        # 定义一个收件人列表
        receivers = ['qazhangfan@163.com','467032459@qq.com']
        # 简单发送没有附件的邮件的方法
        # MIMEText方法有三个参数，第一个参数是内容，第二个参数是内容的类型，第三个参数是内容的编码类型。
        message = MIMEText('<p style="color: red; font-size: 30px">'
                           '这是一封来自Python发送的测试邮件的内容...</p>',
                           'html', 'utf-8')
        message['Subject'] = Header('新年快乐', 'utf-8')
        # 发送带附件的邮件的方法
        # message = MIMEMultipart()
        # message.attach(MIMEText('<p style="color: red; font-size: 30px">'
        #                    '这是一封来自Python发送的测试邮件的内容...</p>',
        #                    'html', 'utf-8'))
        # message['Subject'] = Header('一封Python发送的邮件', 'utf-8')
        # # 构造邮件附件对象
        # att = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
        # att["Content-Type"] = 'application/octet-stream'
        # att["Content-Disposition"] = 'attachment; filename="%s"' % os.path.split(attachment)[1]
        # message.attach(att)
        try:
            smtpObj = smtplib.SMTP()
            # 连接邮件服务器，注意这里是发件人的邮件服务器
            smtpObj.connect('smtp.qq.com', 25)
            # 注意这里是发件人的真实邮箱账号和密码
            smtpObj.login(user='1109355448@qq.com', password='wgzuuljyotjujjge')
            # 发送邮件，注意这个方法没有返回值，我们通过检查其是否抛出SMTPException错误来判断邮件是否发送成功。
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


if __name__ == '__main__':
    # report = Reporter('1.0.2')
    # report.write_report('登录功能', '接口测试', 'TC-001',
    #                     'Agileone的正常登录测试', '成功', '无', '无')
    # report.write_report('登录功能', '接口测试', 'TC-002',
    #                     'Agileone的错误登录测试', '失败', '断言失败', '20190415_123540_cbt.png')
    # report.write_report('需求提案', 'GUI测试', 'TC-002',
    #                     'Agileone的错误登录测试', '错误', '无法连接到服务器', '20190415_123845_cbt.png')
    # report.generate_html()
    # comp_file = report.compress_report()
    # print(comp_file)
    Mail().send_mail()

