#coding:utf-8
'''
Created on 2016年11月10日
@author: wenjing
'''
#必须导入的内容
import sys
curDir = sys.path[0]
print curDir
sys.path.append(curDir + '\\MPTestCases\\common')
sys.path.append(curDir + '/MPTestCases/common')
import Initialize
import CutScreenshot
import InitLogin
import traceback

import unittest
from appium import webdriver
from time import sleep
import Initialize

class MPlogin(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		print '************************** MPlogin test **************************'
	#初始化操作
	def setUp(self):
		Initialize.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Initialize.tearDown(self)
	
	'''手机号登陆：
	1、打开秒拍，进入个人主页
	2、点击登陆弹出登陆对话框
	3、点击手机号登陆，进入手机号登陆界面
	4、点击忘记密码
	5、点击返回到手机号登陆界面
	6、点击注册，点击返回到手机号登陆界面
	7、什么都不输入，点击登陆
	8、输入任意手机号，点击登陆
	9、输入任意手机号，和任意密码，点击登陆
	10、输入正确手机号和错误密码，点击登陆
	11、输入正确手机号和正确密码点击登陆，进入到首页
	12、退出登陆，回到首页'''
		
	def test_Mobilelogin(self):
		try:
			print 'start test_Mobilelogin test ...  '
			Initialize.init_case(self)  #处理开屏广告是否存在的情况
			sleep(5)
			InitLogin.init_logout(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my_lay').click()
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/no_login_views').click()#点击未登录
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/login_phone_button').click()#点击手机号登录
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/captcha_login').click()#点击忘记密码
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()#点击返回
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/login_phone_button').click()#点击手机号登录
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click()
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview').send_keys('13112344321')#输入手机号
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click()	#登录
			sleep(2)	
			self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview').send_keys('13112344321')#输入手机号
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview').send_keys('123456')#输入密码
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click()	#登录
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview').send_keys('13699193860')#输入手机号
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview').send_keys('qwerty')#输入密码
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click()	#登录
			sleep(4)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview').send_keys('13699193860')#输入手机号
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview').send_keys('123456')#输入密码
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click()	#登录
			sleep(2)
			self.driver.swipe(600,1200,600,500)
			sleep(2)
			self.driver.swipe(600,1200,600,500)
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click()#点击设置
			sleep(2)
			self.driver.swipe(600,1200,600,500)
			sleep(2)
			self.driver.swipe(600,1200,600,500)
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/logout_button').click()#点击退出登录
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/dialog_right_buton').click()#点击确定
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()#点击返回
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click()#点击返回
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPlogin('test_Mobilelogin'))  

	runner = unittest.TextTestRunner()  
	runner.run(suite)


