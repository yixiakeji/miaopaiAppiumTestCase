#coding:utf-8
#Edit by liyuanhong 2016/4/12#

#必须导入的内容
import sys
curDir = sys.path[0]
print curDir
sys.path.append(curDir + '\\MPTestCases\\common')
sys.path.append(curDir + '/MPTestCases/common')
import Initialize
import CutScreenshot
import traceback


import unittest
from appium import webdriver
from time import sleep
import Initialize

class MPHotpage(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		print "************************** MPHotpage test **************************"
	'''
	def init_case(self):
		#处理开屏广告是否存在的情况
		try:
			sleep(1)
			el = self.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #获取开屏广告是否存在
			self.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #点击开屏广告上的'点击跳过'按钮
			sleep(2)
		except Exception,ex:
			pass
			'''
		
			
	#初始化操作
	def setUp(self):
		Initialize.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Initialize.tearDown(self)
		
		
	def click_shouye_rebang_faxian_wo(self):
		try:
			'''按钮的点击测试
			1、分别对底导上的首页、热榜、发现，我进行了点击
			'''
			print 'start click_shouye_rebang_faxian_wo test ...  '
			Initialize.init_case(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #点击底导上的首页
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_friend').click() #点击底导上的热榜
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_message_tip').click() #点击底导上的发现
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #点击底导上的首页
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
		
	def switch_category_at_shouye_by_click(self):
		try:
			'''首页平道分类测试
			1、点击切换完首页所有的分类
			'''
			print 'start switch_category_at_shouye_by_click test ...  '
			Initialize.init_case(self)
			sleep(5)
			ele1 = self.driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RadioButton') #获取首页所有的二级分类
			ele1[0].click()
			sleep(2)
			ele1[1].click()
			sleep(2)
			ele1[2].click()
			sleep(2)
			for i in range(0,12):
				ele1[3].click()
				sleep(2)
			ele1[4].click()
			sleep(2)
			ele1[5].click()
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(2)
			self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView').click() #点击关闭全部平道面板
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)

	def switch_Opencategory_at_shouye_by_click(self):
		try:
			'''首页平道分类测试
			1、点击切换完首页展开的频道分类
			'''
			print 'start switch_Opencategory_at_shouye_by_click test ...  '
			Initialize.init_case(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(1)
			ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			for i in range(0,14):
				ele[i].click()
				sleep(1)
				self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
				sleep(1)
			self.driver.swipe(500, 900, 500, 300) #向上滑动
			ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			ele[len(ele) - 1].click()
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(1)
			ele[len(ele) - 2].click()
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(1)
			self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView').click() #点击关闭全部平道面板
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)


	def drag_to_change_category_order(self):
		try:
			'''首页平道分类测试
			1、改变首页分类的顺序
			'''
			print 'start drag_to_change_category_order test ...  '
			Initialize.init_case(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(1)
			ele = self.driver.find_elements_by_id('com.yixia.videoeditor:id/icon')
			self.driver.drag_and_drop(ele[6],ele[8])
			sleep(2)
			self.driver.drag_and_drop(ele[4],ele[2])
			sleep(2)
			self.driver.drag_and_drop(ele[8],ele[2])
			sleep(2)
			self.driver.drag_and_drop(ele[4],ele[10])
			sleep(2)
			self.driver.drag_and_drop(ele[10],ele[1])
			sleep(2)
			self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView').click() #点击关闭全部平道面板
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/more').click() #点击展开频道更多
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
		
		
	def switch_category_at_shouye_by_slide(self):
		try:
			'''切换分类页面
			1、滑动切换完首页所有的分类
			'''
			print 'start switch_category_at_shouye_by_slide test ...  '
			Initialize.init_case(self)
			sleep(5)
			for i in range(0,20):
				self.driver.swipe(700, 900, 50, 900) #向右滑动
				sleep(2)
			for i in range(0,20):
				self.driver.swipe(50, 900, 700, 900) #向左滑动
				sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
		
		
		
		
def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(MPHotpage('click_shouye_rebang_faxian_wo'))
	suite.addTest(MPHotpage('switch_category_at_shouye_by_slide'))
	suite.addTest(MPHotpage('switch_category_at_shouye_by_click'))
	suite.addTest(MPHotpage('switch_Opencategory_at_shouye_by_click'))
	suite.addTest(MPHotpage('drag_to_change_category_order'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)
