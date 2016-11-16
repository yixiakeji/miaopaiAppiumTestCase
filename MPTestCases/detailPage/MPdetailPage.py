#coding:utf-8
'''
Created on 2016年10月12日
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
class MPdetailPage(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		print '************************** MPdetailPage test **************************'

	#初始化操作
	def setUp(self):
		Initialize.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Initialize.tearDown(self)

	def test_check_like(self):
		try:
			print 'start test_check_like test ...  '
			Initialize.init_case(self)  #处理开屏广告是否存在的情况
			InitLogin.init_login(self)  #如果没有登陆则登陆秒拍
			sleep(5)
			#手机号登陆
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_record').click()
			sleep(5)
			try:
				self.driver.find_element_by_id('com.yixia.videoeditor:id/login_phone_button').click()
				sleep(5)
				self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview').send_keys('13699193860')
				sleep(5)
				self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview').send_keys('123456')
				sleep(5)
				self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').is_enabled()
				self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click()
				sleep(10)
			except:
				self.driver.keyevent('4')
				print'...........'
				sleep(10)
				
			#我的界面获取用户昵称
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my_lay').click()
			sleep(5)
			nickName=self.driver.find_element_by_id('com.yixia.videoeditor:id/nickname').text
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click()
			#点击热门第一个视频
			sleep(5)
			ele=self.driver.find_elements_by_id('com.yixia.videoeditor:id/cover')
			ele[0].click()
			sleep(2)
			#点击单列第一个视频
			ele=self.driver.find_elements_by_id('com.yixia.videoeditor:id/content')
			ele[0].click()
			sleep(5)
			#双击点赞
			l1=self.driver.find_element_by_id('com.yixia.videoeditor:id/video_layout')
			x=int (l1.location.get('x')+200)
			y=int (l1.location.get('y')+200)
			self.driver.tap([(x,y)], 100)
			self.driver.tap([(x,y)], 100)
			print 'double click'
			sleep(5)
			#点击第一个头像进入对比用户昵称
			self.driver.find_element_by_id('com.yixia.videoeditor:id/good_fold_parent_layout').click()
			sleep(5)
			self.driver.scroll(self.driver.find_element_by_id('com.yixia.videoeditor:id/good_fold_parent_layout'), self.driver.find_element_by_id('com.yixia.videoeditor:id/content'))
			sleep(5)
			ele=self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			ele[1].click()
			sleep(5)
			self.assertEquals(nickName,self.driver.find_element_by_id('com.yixia.videoeditor:id/nickname').text)  
			sleep(5)
			self.driver.keyevent('4')
			sleep(5)
			#取消点赞
			self.driver.find_element_by_id('com.yixia.videoeditor:id/good_send').click()
			sleep(5)
			ele=self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			ele[0].click()
			sleep(5)
			self.assertNotEquals(nickName,self.driver.find_element_by_id('com.yixia.videoeditor:id/nickname').text)  
			sleep(5)
			self.driver.keyevent('4')
			sleep(5)
			#点赞
			self.driver.find_element_by_id('com.yixia.videoeditor:id/good_send').click()
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/good_fold_parent_layout').click()
			sleep(5)
			#评论部分
			self.driver.find_element_by_id('com.yixia.videoeditor:id/comment_input').click()
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/send_text').is_enabled();
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/comment_input').send_keys('6666')
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/send_text').is_enabled()
			self.driver.find_element_by_id('com.yixia.videoeditor:id/send_text').click()
			sleep(5)
			self.driver.keyevent('4')
			self.driver.keyevent('4')
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
		

def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPdetailPage('test_check_like'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)