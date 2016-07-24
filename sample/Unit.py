#-*- coding: UTF-8 -*- 
#import unittest
from unittest import TestCase
class Unit(TestCase):
     ##初始化工作   
    def setUp(self):  
        pass  
    #退出清理工作   
    def tearDown(self):  
        pass  
    #具体的测试用例，一定要以test开头   
    def testsum(self):
        sum=7+8
        self.assertEqual(sum, 15, 'test sum fail')  
         
          
    def testsub(self):
        sub=10-3
        self.assertEqual(sub, 7, 'test sub fail')  
# if __name__ =='__main__':  
#      TestCase.run();
