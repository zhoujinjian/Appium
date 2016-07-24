#-*- coding: UTF-8 -*- 
from appium import webdriver
from time import sleep
from appium.webdriver.webelement import WebElement

project_path="E:\mytesting\AppiumPython"
class ZhiHuTestCase(object):
    
    def startApp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '192.168.56.111:5555'
        desired_caps['app'] = 'C:\\Users\\lixionggang\\Desktop\\zhihu.apk'
        desired_caps['appPackage'] = 'com.zhihu.android'
        desired_caps['appActivity'] = 'com.zhihu.android.ui.activity.GuideActivity'
        desired_caps['unicodeKeyboard']='True'
        desired_caps['resetKeyboard']='True'
        desired_caps['noSign']='True'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def login(self):
        
        login_or_reg=self.driver.find_element_by_name("登录或注册")
        login_or_reg.click()
        
        username=self.driver.find_element("id","com.zhihu.android:id/email_or_phone")
        username.send_keys("crazysand_001@163.com")
        
        password=self.driver.find_element("id","com.zhihu.android:id/password")
        password.send_keys("123456")
       
        #loginBtn=self.driver.find_element("id", "com.zhihu.android:id/btn_confirm")
#         login_btn=self.driver.find_element("xpath","//android.widget.Button[@text='登录']")
#         login_btn.click()

        #find_elements返回多个定位到的元素，存放在list里
        login_btn_list=self.driver.find_elements("name","登录")
        for btn in login_btn_list:
            print btn.get_attribute("text")
            print type(btn)
        login_btn_list[1].click()
        sleep(7)
        cur_activity=self.driver.current_activity
        print type(cur_activity)
        print cur_activity
        if cur_activity==".ui.activity.MainActivity":
            print "登录成功"
        else:
            print "登录失败"
        source=self.driver.page_source
        print source
        if u"首页" in source:
            print "登录成功"
        else:
            print "登录失败"
        
        self.driver.swipe(540, 1500, 540, 500, 500)
        sleep(3)
        self.driver.get_screenshot_as_file(project_path+"\\images\\python.png")
        self.driver.keyevent(4)
    def quit(self):
        self.driver.quit()
zhihu=ZhiHuTestCase()
zhihu.startApp()
zhihu.login()
zhihu.quit()