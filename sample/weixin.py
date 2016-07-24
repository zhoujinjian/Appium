#-*- coding: UTF-8 -*- 
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction


class Weixin(object):
    
    #启动app
    def startApp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'deivce'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #sleep(5)
        #self.driver.implicitly_wait(5);
        print self.driver.get_window_size()['width']
        print self.driver.get_window_size()['height']
        
    #英文版本下的添加公众号
    def add_public(self,weixinId):
        idlist=["S_Training","alibabatech","shimianduwu"]

        for id in idlist:
            adresslist = WebDriverWait(self.driver,10).until(lambda x:x.find_element("name","Contacts"))
#             aa=TouchAction(self.driver)
#             aa.tap(adresslist).release().perform()
        
            adresslist.click()
            pbc=WebDriverWait(self.driver,10).until(lambda x:x.find_element("name","Official Accounts"))
             
            pbc.click()
            add_btn=WebDriverWait(self.driver,10).until(lambda x:x.find_element("name","Add"))
             
            add_btn.click()
            WebDriverWait(self.driver,10).until(lambda x:x.find_element("xpath","//android.widget.RelativeLayout/android.widget.TextView[1]")).click()
            
             
            text=WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_class_name("android.widget.EditText"))
#             strtext=text.get_attribute('text')
#             self.driver.keyevent(123)   
#             text.click()    
#             for i in range(0,len(strtext)):
#                 self.driver.keyevent(67)
#                 print "shanchu"
            #text.send_keys(id)
            text.set_text(id)
 
			#点击输入法上的搜索
            self.driver.tap([[750,960]])
            sleep(2)
			#点击查询出来的公众号
            self.driver.tap([[455,250]])
			#点击关注
            WebDriverWait(self.driver,10).until(lambda x:x.find_element("name","Follow")).click()
            WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_class_name("android.widget.ImageView")).click()
            self.driver.keyevent(4);
            
        
            
    def quit(self):
        self.driver.quit()
weixin=Weixin()
weixin.startApp()
try:
    weixin.add_public("shimianduwu")
finally:
    weixin.quit()

