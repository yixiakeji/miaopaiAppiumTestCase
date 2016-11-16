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
import InitLogin
import traceback


import unittest
from appium import webdriver
from time import sleep
import Initialize

class MPmypage(unittest.TestCase):
	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		print "************************** MPmypage test **************************"

		
	
	#初始化操作
	def setUp(self):
		Initialize.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Initialize.tearDown(self)
		
		
		'''意见反馈
		1、意见反馈页面没有输入任何内容的情况下点击发送
		2、输入意见反馈后点击发送
		3、全选所有的问题点击发送
		4、输入错误的qq号和意见点击发送
		5、输入正确的qq号和意见点击发送
		6、输入错误的邮箱和意见点击发送
		7、输入正确的邮箱和意见点击发送
		'''
	def test_feedback(self):
		try:
			print 'start test_feedback test ...  '
			Initialize.init_case(self)
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click() #点击底导的我
			sleep(2)
			self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/feedback_layout').click() #点击吐槽不爽
			sleep(2)
			#1、直接点击发送按钮#
			self.driver.find_element_by_name('发送').click()  #点击发送按钮
			sleep(2)

			#2、输入意见反馈点击发送按钮#
			e1 = self.driver.find_element_by_id('com.yixia.videoeditor:id/edit_idea')
			e1.click()  #选中反馈对话框
			sleep(1)
			e1.send_keys('1234567890')
			sleep(0.5)
			self.driver.press_keycode(66)  #按回车键
			sleep(0.5)
			self.driver.find_element_by_name('发送').click()  #点击发送按钮
			sleep(5)

			#3、全选所有问题县级发送按钮#
			self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/feedback_layout').click() #点击吐槽不爽
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/checkBox').click()  #选中经常闪退
			sleep(0.5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/checkBox2').click()  #选中无法播放
			sleep(0.5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/checkBox3').click()  #选中剪辑不方便
			sleep(0.5)
			self.driver.swipe(200,1000,200,100,1000) #向上滑动页面
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/checkBox4').click()  #选中画面不清晰
			sleep(0.5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/checkBox5').click()  #选中看视频卡
			sleep(0.5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/checkBox6').click()  #选中其他
			sleep(0.5)
			self.driver.find_element_by_name('发送').click()  #点击发送按钮
			sleep(2)


			#4、输入错误的QQ号和正确的意见反馈点击发送#
			self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/feedback_layout').click() #点击吐槽不爽
			sleep(2)
			e1 = self.driver.find_element_by_id('com.yixia.videoeditor:id/edit_idea')
			e1.click()  #选中反馈对话框
			sleep(1)
			e1.send_keys('1234567890')
			sleep(0.5)
			self.driver.press_keycode(66)  #按回车键
			sleep(0.5)
			self.driver.press_keycode(4)  #点击返回按钮收起键盘
			sleep(0.5)
			e2 = self.driver.find_element_by_id('com.yixia.videoeditor:id/qq_e_mail')
			e2.click()  #点击您的邮箱/qq
			sleep(0.5)
			e2.send_keys('1234')
			sleep(0.5)
			#self.driver.press_keycode(66)  #按回车键
			#sleep(0.5)
			#self.driver.press_keycode(4)  #点击返回按钮收起键盘
			#sleep(2)
			self.driver.find_element_by_name('发送').click()  #点击发送按钮
			sleep(1)

			#5、输入正确的QQ号和正确的意见反馈点击发送#
			e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/qq_e_mail')
			e3.click()  #点击您的邮箱/qq
			sleep(0.5)
			e3.send_keys('1234567')
			sleep(0.5)
			#self.driver.press_keycode(66)  #按回车键
			#sleep(0.5)
			#self.driver.press_keycode(4)  #点击返回按钮收起键盘
			#sleep(0.5)
			self.driver.find_element_by_name('发送').click()  #点击发送按钮
			sleep(2)

			#6、输入错误的邮箱点和正确意见反馈点击发送#
			self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/feedback_layout').click() #点击吐槽不爽
			sleep(2)
			e1 = self.driver.find_element_by_id('com.yixia.videoeditor:id/edit_idea')
			e1.click()  #选中反馈对话框
			sleep(1)
			e1.send_keys('1234567890')
			sleep(0.5)
			#self.driver.press_keycode(66)  #按回车键
			#sleep(0.5)
			#self.driver.press_keycode(4)  #点击返回按钮收起键盘
			#sleep(0.5)
			e2 = self.driver.find_element_by_id('com.yixia.videoeditor:id/qq_e_mail')
			e2.click()  #点击您的邮箱/qq
			sleep(0.5)
			e2.send_keys('abcd')
			sleep(0.5)
			self.driver.press_keycode(66)  #按回车键
			sleep(0.5)
			self.driver.press_keycode(4)  #点击返回按钮收起键盘
			sleep(0.5)
			self.driver.find_element_by_name('发送').click()  #点击发送按钮
			sleep(1)

			#7、输入正确的邮箱点和正确意见反馈点击发送#
			e2 = self.driver.find_element_by_id('com.yixia.videoeditor:id/qq_e_mail')
			e2.click()  #点击您的邮箱/qq
			sleep(0.5)
			e2.send_keys('abcd@example.com')
			sleep(0.5)
			self.driver.press_keycode(66)  #按回车键
			sleep(0.5)
			self.driver.press_keycode(4)  #点击返回按钮收起键盘
			sleep(0.5)
			self.driver.find_element_by_name('发送').click()  #点击发送按钮
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)


	#测试我的页面，顶部信息栏元素的点击
	def test_mypage_topinfo_click(self):
		try:
			print 'start test_mypage_topinfo_click test ...  '
			Initialize.init_case(self)  #处理开屏广告是否存在的情况
			InitLogin.init_login(self)  #如果没有登陆则登陆秒拍
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click()  #点击底导上的我进入我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/icon_header').click()  #点击个人信息上面的头像
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/imageview').click()  #点击关闭头像
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/user_info_layout').click()  #点击整条用户信息进入个人页面
			sleep(2)
			self.driver.press_keycode('4')  #点击返回按钮返回到我的页面
			sleep(2)
			self.driver.find_element_by_name('申请认证').click()  #点击申请认证
			sleep(2)
			self.driver.press_keycode('4')  #点击返回按钮返回到我的页面
			sleep(3)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/videos_layout').click()  #点击整条视频缩略图区域进入我的个人主页
			sleep(2)
			self.driver.press_keycode('4')  #点击返回按钮返回到我的页面
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)

	#点击完我的页面下，用户信息栏下的所有选项
	def test_mypage_under_tipinfo_items_click(self):
		try:
			print 'start test_mypage_under_tipinfo_items_click test ...  '
			Initialize.init_case(self)  #处理开屏广告是否存在的情况
			InitLogin.init_login(self)  #如果没有登陆则登陆秒拍
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click()  #点击底导上的我进入我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/follow_layout').click()  #点击进入关注列表页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/fans_layout').click()  #点击粉丝进入到粉丝列表页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/message_layout').click()  #点击进入消息通知页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/push_layout').click()  #点击进入今日推送页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/free_videos_layout').click()  #点击进入免流量视频页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/likevideos_layout').click()  #点击进入赞过的视频页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/video_history_layout').click()  #点击进入播放历史页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/draft_layout').click()  #点击进草稿箱页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/topic_layout').click()  #点击进入我关注的话题页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/money_layout').click()  #点击进入红包页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/reward_layout').click()  #点击进入悬赏页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/feedback_layout').click()  #点击进入吐槽不爽页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.swipe(200,1000,200,100,1000) #我的页面向上滑动
			sleep(1)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click()  #点击进入设置页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click()  #点击回到热门页面
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)

	#点击完消息页面的所有item项
	def test_message_items_all_click(self):
		try:
			print 'start test_message_items_all_click test ...  '
			Initialize.init_case(self)  #处理开屏广告是否存在的情况
			InitLogin.init_login(self)  #如果没有登陆则登陆秒拍
			sleep(5)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click()  #点击底导上的我进入我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/message_layout').click()  #点击进入消息通知页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_newfriend').click()  #点击进入新的好友消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_like').click()  #点击进入赞页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_comment').click()  #点击进入评论消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_at').click()  #点击进入@我的消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/rl_notification').click()  #点击进入系统消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到消息页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
			sleep(2)
			self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click()  #点击回到热门页面
			sleep(2)
		except Exception,e:
			print traceback.format_exc()
			CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)





def suite(self):
	suite = unittest.TestSuite()  
	#测试意见反馈功能
	suite.addTest(MPmypage('test_feedback'))
	suite.addTest(MPmypage('test_mypage_topinfo_click'))
	suite.addTest(MPmypage('test_mypage_under_tipinfo_items_click'))
	suite.addTest(MPmypage('test_message_items_all_click'))

	runner = unittest.TextTestRunner()  
	runner.run(suite)