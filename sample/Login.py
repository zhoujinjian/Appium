# -*- coding: UTF-8 -*-
from appium import webdriver
from time import sleep


class Login(object):

    def startapp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'f0be4397'
        desired_caps['appPackage'] = 'com.ghhy.tcpay'
        desired_caps['appActivity'] = 'com.qdcf.pay.aty.main.login.LoginActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        # desired_caps['noSign']='True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def login(self):

        self.driver.find_element_by_id("com.ghhy.tcpay:id/email").click()
        self.driver.find_element_by_id("com.ghhy.tcpay:id/email").send_keys("13651276145")

        self.driver.find_element_by_id("com.ghhy.tcpay:id/password").click()
        self.driver.find_element_by_id("com.ghhy.tcpay:id/password").send_keys("11111111")

        self.driver.find_element_by_id("com.ghhy.tcpay:id/sign_in_button").click()

        cur_activity = self.driver.current_activity
        print type(cur_activity)
        print cur_activity

        if cur_activity == "com.qdcf.pay.aty.main.UserActivity":
            print u"登录成功"
        else:
            print u"登录失败"
        source = self.driver.page_source
        print source
        self.driver.swipe(540, 1500, 540, 500, 500)
        sleep(3)
        self.driver.get_screenshot_as_file("D:\\images\\python.png")
        self.driver.keyevent(4)

    def quit(self):
        self.driver.quit()

login = Login()
login.startapp()
login.login()
login.quit()


