#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import threading
import subprocess
import socket


# 1.首先先通过命令adb devices来去查询我们当前系统下连接了多少台设备
# 2.依据上面命令的执行结果提取并获得设备名列表
# 3.接下来再通过命令adb -s device_name shell getprop ro.build.version.release来去查询指定设备的系统版本
# 4.然后我们需要分别构造两个端口，然后去检查这两个端口是否已经被占用了，
# 如果占用，那么我们让这个端口号自增1，然后再检查，直到找到一个没有被占用的端口为止。
# 5.上述两个端口分别对应appium启动时候的-p和-bp两个参数的值。
# 6.端口是否被占用我们需要通过建立socket连接来确定。
# 这里建立的连接都是tcp连接，利用socket的connect/connect_ex方法都可以来检测。
# 前一个方法如果端口没有被占用，它会抛出socket.error类型的错误。
# 后一个方法如果端口没有被占用，它不会跑出错误，它是正常连接上之后，方法本身会返回0这个值。
# 7.接下来我们就需要构造并执行appium server的启动命令
# 8.这个命令是 appium -a 127.0.0.1 -p port -bp bp-port --device-name device_name --platform-version system_version
# --log file_path --log-level info --log-timestamp
from jiaoben.tuxiang.report.onestroketest import OneStrokeTest


class MobileCloud:

    # 计划此方法将来返回设备信息列表，这个列表的每一个元素（deviceName，platformVersion，port，bpport）。
    def get_device_info(self):
        port = 5000
        bp_port = 8000
        list = []
        devices = subprocess.check_output('adb devices').decode().strip().split('\r\n')
        for i in range(1, len(devices)):
            device_name = devices[i].split('\t')[0].strip()
            platform_version = subprocess.check_output(
                'adb -s %s shell getprop ro.build.version.release' % device_name).decode().strip()
            port = self.find_port(port)
            bp_port = self.find_port(bp_port)
            list.append((device_name, platform_version, port, bp_port))
            # 下面这两行端口自增的目的是要让新的设备使用新的端口，刚才找到的可用端口已经提前预定过了。
            port += 1
            bp_port += 1
        return list

    # 定义一个查找当前系统可用端口的方法
    def find_port(self, port):
        # 这里check_port方法用来检查端口是否已经占用，如果已经占用，我们在while循环中让端口号加1，
        # 然后继续利用此方法检查，直到找到一个没有被占用的端口为止。
        while self.check_port(port):
            port += 1
        return port

    # 定义一个检查端口是否已经占用的方法
    def check_port(self, port):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con.connect(('127.0.0.1', port))
            con.shutdown(socket.SHUT_RDWR)
            return True
        except socket.error:
            return False

    # 定义启动appium server的方法
    def start_appium(self, device_name, platform_version, port, bp_port):
        # 构造appium执行日志文件的路径
        log_path = os.path.join(os.getcwd(), 'report/%s_appium.log' % device_name)
        # 构造命令 appium -a 127.0.0.1 -p port -bp bp-port --device-name device_name --platform-version system_version
        # --log file_path --log-level info --log-timestamp
        cmd = 'appium -a 127.0.0.1 -p %d -bp %d --device-name %s --platform-version %s --log %s --log-level info --log-timestamp' % (
            port, bp_port, device_name, platform_version, log_path)
        # 执行命令
        os.system(cmd)


if __name__ == '__main__':
    os.system('taskkill /f /im node.exe')
    mc = MobileCloud()
    devices = mc.get_device_info()
    threads = []
    for i in range(len(devices)):
        # 构造appium server和脚本的多线程
        ost = OneStrokeTest(devices[i][0], devices[i][1], devices[i][2])
        server_thread = threading.Thread(target=mc.start_appium, args=(*devices[i],), name='server-%d' % i)
        client_thread = threading.Thread(target=ost.start_test, name='client-%d' % i)
        threads.append(server_thread)
        threads.append(client_thread)
    # threads: server-0, client-0, server-1, client-1，但是我们希望获得的排序是 server-0, server-1, client-0, client-1
    # def sorted(t):
    #   return t.getName()[0 : 1]
    # 利用线程名的首字母进行排序
    threads.sort(key=lambda t: t.getName()[0: 1], reverse=True)
    for t in threads:
        if 'client-0' in t.getName():
            time.sleep(35)
        # 设置当前线程为守护线程
        t.setDaemon(True)
        t.start()
    for t in threads:
        if 'client' in t.getName():
            # 设置当前线程需要阻塞
            t.join()
    os.system('taskkill /f /im node.exe')
    print('*********** 全部测试完成 *************')
    # 我们代码写好后的出错处理
    # 1.发现报urllib3连不上的错误，修改了port初始值，
    # 还改了webdriver.Remote(self.url, self.desired_caps)，这个必须运行在appium server启动之后
    # 经过尝试和分析，我们发现修改port值是无效修改，第二个修改没错。
    # 2.发现报killtask不是内部命令的错误，这个是因为正确的命令是taskkill
    # 3.发现在跑的时候两个设备，5.0版本的能够正常执行，但是4.0版本的每一次感觉都没有把代码执行完，
    # 经过分析发现，主要是由于4.0版本的执行速度有点慢，导致我们原有的隐式等待60秒仍然找不到该找的元素，
    # 所以我们在执行慢的画面加了一个强制等待，然后验证发现没有问题了。
    # 但是这个地方我们更好地做法应该把它再优化为显示等待，这样稳定性一定会更好。
