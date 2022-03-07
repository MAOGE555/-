import re
import time
# class a():
#     def cao(self):
#         cao = 'aaaaaaaaa'
#         print('aaaaa')
# class b():
#     q = a()
#     print(q.cao)
#     def wo(self):
#         hh = '11'
#         cc = hh
#         print(cc)
# c = b()
# print(c)
# import requests
# class weilai():
#     # def __init__(self):
#         #print("这是进入神秘世界的必经通道")
#     def zhixing(self):
#         header = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
#         try:
#             ggg='http://www.baidu.com'
#             a = requests.get(url=ggg, headers=header, timeout=(1.5, 2.5), allow_redirects=False)
#             print(a)
#         except:
#             print("报错了")
# class testsss(weilai):
#     def wocao(self):
#         print("欢迎来到卧槽的世界，我的小bug")
#         self.zhixing()
# class maoge(testsss):
#     def wo(self):
#         print('first')
#         self.wocao()
# a = maoge()
# print(a.wo())
# class mao():
#     def aaa(self):
#         print('aa')
#
# def Simple_filtering():  # 过滤url后面的内容，只留http+域名
#     url = str(input("请输入:"))
#     time.sleep(0.2)
#     url.strip('\n')  # 去掉换行
#     if "http" in url:  # 如果http的存在，就过滤掉，不留端口，只留http+域名
#         list = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
#         url_pro = ' '.join(list)
#         return url_pro
#     else:  # 只留IP,过滤的是192.168.0.1:88
#         if 'www' in url:  # 如果存在www.baidu.com:80/asdga/gasd或者www.baidu.com/aaagsd  这样情况，滚去上面的，过滤端口
#             print("小伙子，你真是哪壶不开提哪壶，加上http://去重试")
#         elif '.com' in url:
#             print("小伙子，你真是哪壶不开提哪壶，加上http://去重试")
#         elif '.cn' in url:
#             print("小伙子，你真是哪壶不开提哪壶，加上http://去重试")
#         elif '.net' in url:
#             print("小伙子，你真是哪壶不开提哪壶，加上http://去重试")
#         elif '.org' in url:
#             print("小伙子，你真是哪壶不开提哪壶，加上http://去重试")
#         else:
#             list = re.findall("((?:[0-9]{1,3}\.){3}[0-9]{1,3})", url)  # 过滤ip专用，192.168.0.1:8888，秒变成192.168.0.1
#             print("第二种结果，ip的过滤")
#             url_pro = ' '.join(list)
#             # print(url_pro)
#             return url_pro
# def IP():#只留IP的
#     a = Simple_filtering()
#     if "https" in a:
#         one = a[8:]
#         return one
#     elif "http" in a:
#         two = a[7:]
#         return two
#     else:
#         print("有问题啊扑街仔?")
from subprocess import run
import os
import subprocess

import re


def check_ip(ipAddr):
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        print('真')
    else:
        print('假')
if __name__ == '__main__':
    a = str(input('aaa:'))
    check_ip(a)
    #a = "./tools/shiro/shiro_attack_2.2 && javaw -jar shiro_attack-2.2.jar"
    #a = run("./tools/shiro/shiro_attack_2.2 && javaw -jar shiro_attack-2.2.jar",shell=True)
    # print(a)
    # a = os.popen('cd tools\\shiro\\shiro_attack_2.2\\ && javaw -jar shiro_attack-2.2.jar')
    # print(a)
    # cmd = 'cd tools\\shiro\\shiro_attack_2.2\\ && javaw -jar shiro_attack-2.2.jar'
    # subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)




    # print(IP())
    #I need 只有ip的，只有域名
    #two 留http://www.baidu.com的结果，和http://baidu.com:90/
    #three 域名的结果，baidu.com

    # a = mao()
    # print(a.aaa())
    # string = str(input("aaa:"))
    # url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    # print(url)

    # test = '192.168.20.1:66/2sgasg'
    # list = re.findall("((?:[0-9]{1,3}\.){3}[0-9]{1,3})", test)
    #
    # print(list)  # 获取ip地址