# -*- coding: utf-8 -*-
__author__ = 'florije'

import urllib, urllib2, cookielib
import re
import datetime


class Loginjx:
    # 伪装browser
    header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    username = ''
    passwd = ''
    cookie = None  #cookie对象
    cookiefile = './cookies.dat'  #cookie临时存放地
    user = ''

    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd
        #cookie设置
        self.cookie = cookielib.LWPCookieJar()  #自定义cookie存放
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)

        #登陆

    def login(self):

        #请求参数设置
        postdata = {
            'username': self.username,
            'password': self.passwd,
            'cookietime': 2592000,
            'dosubmit': '登录',
            'forward': ''
        }
        postdata = urllib.urlencode(postdata)

        #发起请求
        req = urllib2.Request(
            url='http://www.gjjx.com.cn/index.php?m=member&c=index&a=login',
            data=postdata,  #请求数据
            headers=self.header  #请求头
        )

        result = urllib2.urlopen(req).read()
        result = str(result)
        self.user = self.username

        self.cookie.save(self.cookiefile)  #保存cookie

        if '登陆成功' in result:
            print("%s 你已成功登陆。---------\n" % (self.user))
            flag = True
        else:
            print("%s 登陆可耻的失败鸟")
            flag = False

        return flag

    def get_uid(self):
        uid_url = urllib2.Request(
            url='http://www.gjjx.com.cn/index.php?m=member&c=index&a=appointment',
            headers=self.header
        )
        auth = urllib2.urlopen(uid_url).read()
        result = str(auth)
        uid = re.findall('''学员证号<span>(\d+)</span>''', result)
        return uid[0]

    def order_class(self, uid="61394720", yyrq="25-DEC-11", sd="5", cnbh="32220", traint="2"):
        base_url = "http://www.gjjx.com.cn/index.php?m=member&c=index&a=bpk&"
        query_param = "id=%s&yyrq=%s&sd=%s&cnbh=%s&traint=%s" % (uid, yyrq, sd, cnbh, traint)
        print base_url + query_param
        uid_url = urllib2.Request(
            url=(base_url + query_param),
            headers=self.header
        )
        auth = urllib2.urlopen(uid_url).read()
        result = str(auth)
        if "过期" in result:
            return "timeout"
        elif "成功" in result:
            return "ok"
        elif "同一车时不能重复预约" in result:
            return "ok"
        else:
            return "failed"


print("Requesting......")
# 用户名密码
login = Loginjx('username', 'password')
#时段 5 - 07:00--12:00 6 - 13:00--18:00
sd = "5"
#场内编号
cnbh = "32221"
#预约日期
order_date = '2011-12-25'
yyrq = datetime.datetime.strptime(order_date, '%Y-%m-%d').strftime('%d-%b-%y').upper();
#yyrq="25-DEC-11"
#科目类别 0 桩训 2 模拟 ....
traint = "2"

flag = False
order_ok = False

while flag == False:
    flag = login.login()
    if flag:
        uid = login.get_uid()
        while order_ok == False:
            result = login.order_class(uid=uid, yyrq=yyrq, sd=sd, cnbh=cnbh, traint=traint)
            if result == "timeout":
                print("超时！重新登录！")
                flag = False
                order_ok = False
            elif result == "failed":
                print("正在不断尝试")
                pass
            else:
                order_ok = True
                flag = True
                print("不小心成约车功了！！")