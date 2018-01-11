# -*- coding: utf-8 -*-
"""
@author: liuyw
@change : huangbh
"""
from splinter.browser import Browser
from selenium import webdriver
from time import sleep
import traceback
import time, sys
import os



class huoche(object):
    """docstring for huoche"""
    driver_name = ''
    executable_path = ''
    # 用户名，密码
    username = u"yourusername"
    passwd = u"yourpassword"
    # cookies值得自己去找, 下面两个分别是上海, 太原南
    #上海   u"%u4E0A%u6D77%2CSHH"
    # 太原南  u"%u592A%u539F%2CTYV"
    starts =u"%u4E0A%u6D77%2CSHH"
    ends = u"%u592A%u539F%2CTYV"
    # 时间格式2018-01-19
    #2018-01-15
    dtime = u"2018-02-13"
    # 2018-01-24
    # dtime = u"2018-02-22"
    # 车次，选择第几趟，0则从上之下依次点击
    order = 0
    ###乘客名
    users = [u"名字1", u"名字2"]
    ##席位
    #默认
    xb = u"硬卧（￥322.5）"
    #xb=  u"硬座（￥189.5）"
    pz = u"成人票"


    """网址"""
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    buy = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    login_url = 'https://kyfw.12306.cn/otn/login/init'

    def __init__(self):
        # self.driver_name = 'chrome'
        # self.executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'
        # self.executable_path = '/usr/local/bin/chromedriver'
        self.driver_name='firefox'
        self.executable_path='D:\Program Files\Mozilla Firefox\geckodriver'

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill("loginUserDTO.user_name", self.username)
        # sleep(1)
        self.driver.fill("userDTO.password", self.passwd)
        print(u"等待验证码，自行输入...")
        while True:
            if self.driver.url != self.initmy_url:
                sleep(1)
            else:
                break

    def start(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        self.driver.driver.set_window_size(1400, 1000)
        self.login()
        # sleep(1)
        self.driver.visit(self.ticket_url)
        # 加载查询信息
        self.driver.cookies.add({"_jc_save_fromStation": self.starts})
        self.driver.cookies.add({"_jc_save_toStation": self.ends})
        self.driver.cookies.add({"_jc_save_fromDate": self.dtime})

        bookSuccess=False
        while(bookSuccess==False):
            self.driver.visit(self.ticket_url)
            bookSuccess= self.callbystart()
        print(u"购票成功...")


    def callbystart(self):
        try:
            print(u"购票页面开始...")
            # sleep(1)
            self.driver.reload()
            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print(u"循环点击查询... 第 %s 次" % count)
                    # sleep(1)
                    try:
                        self.driver.find_by_text(u"预订")[self.order - 1].click()
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订")
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text(u"查询").click()
                    count += 1
                    print(u"循环点击查询... 第 %s 次" % count)
                    # sleep(0.8)
                    try:
                        for i in self.driver.find_by_text(u"预订"):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print(u"还没开始预订 %s" % count)
                        continue
            print(u"开始预订...")

            # sleep(3)
            # self.driver.reload()
            sleep(1)
            print(u'开始选择用户...')

            for user in self.users:
                self.driver.find_by_text(user).last.click()

            print(u"提交订单...")
            sleep(1)

            for i in self.driver.find_by_text(self.pz):
                i.click()
            # # sleep(1)
            for i in self.driver.find_by_text(self.xb):
                i.click()
            # sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            # print u"开始选座..."

            sleep(1.5)
            print( u"确认选座...")
            self.driver.find_by_id('qr_submit_id').click()
            bookSuccess=True
            return bookSuccess
        except Exception as e:
            print (e)
            #很抱歉，无法提交您的订单!
            #原因： 您选择了2位乘车人，但本次列车硬卧仅剩1张。
            bookSuccess = False
            return bookSuccess

if __name__ == '__main__':
    huoche = huoche()
    huoche.start()