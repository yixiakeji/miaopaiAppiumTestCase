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

class MPHotpageBanner(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self, methodName)
        print "************************** MPBanner_test test **************************"

    #初始化操作
	def setUp(self):
		Initialize.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Initialize.tearDown(self)

    def test_banner(self):
		try:
			print 'start test_banner test ...  '
			Initialize.init_case(self)  #处理开屏广告是否存在的情况
			InitLogin.init_login(self)  #如果没有登陆则登陆秒拍
			sleep(7)
			#查找banner翻页元素获取banner总页数
			eles=self.driver.find_elements_by_xpath('//android.widget.LinearLayout[contains(@id,com.yixia.videoeditor:id/banner_dots_layout)]/android.widget.ImageView')
			l=len(eles)*2
			print l
			#获取banner元素
			banner=self.driver.find_element_by_id('com.yixia.videoeditor:id/banner_img')
			#向左滑动banner总数*2次
			width=self.driver.get_window_size().get('width')
			height=self.driver.get_window_size().get('height')
			#print width
			#print height
			x_start=540*width/720
			x_end=160*width/720
			y=450*height/1280
			for i in range(0,l):
				self.driver.swipe(x_start, y, x_end, y)
				sleep(2)
			#向左滑动banner总数*2次
			for i in range(0,l):
				self.driver.swipe(160, 450,546, 409)
				sleep(2)
			sleep(5)
			#点击任一banner
			banner.click()
			self.driver.keyevent('4')
			sleep(5)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)

def suite(self):
     suite = unittest.TestSuite()  
     suite.addTest(MPHotpageBanner('test_banner'))
     runner = unittest.TextTestRunner()  
     runner.run(suite)       
        