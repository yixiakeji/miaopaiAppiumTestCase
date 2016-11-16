#coding:utf-8
#Edit by liyuanhong 2016/10/20#

from time import sleep

def init_login(self):
	#处理未登陆的情况
	sleep(5)
	self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my_lay').click() #点击底导上的我
	sleep(2)
	try:
		self.driver.find_element_by_id('com.yixia.videoeditor:id/no_login_views').click() #点击我的页面顶部的个人信息栏弹出登陆对话框
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/login_phone_button').click() #点击手机号登陆
		sleep(2)
		#5、输入手机号
		e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/phone_textview')
		e3.click()  #点击手机号输入框弹出键盘
		sleep(0.5)
		e3.send_keys('13699193860')
		sleep(2)
		#5、输入密码
		e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/password_textview')
		e3.click()  #点击密码输入框弹出键盘
		sleep(0.5)
		#e3.send_keys('123456')
		self.driver.keyevent(8)
		sleep(0.5)
		self.driver.keyevent(9)
		sleep(0.5)
		self.driver.keyevent(10)
		sleep(0.5)
		self.driver.keyevent(11)
		sleep(0.5)
		self.driver.keyevent(12)
		sleep(0.5)
		self.driver.keyevent(13)
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/login_button').click() #点击登陆
		sleep(2)
		try:
			self.driver.find_element_by_id('com.yixia.videoeditor:id/skip').click() #手机号绑定页面点击跳过
			sleep(2)
		except:
			pass
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #点击首页回到首页
		sleep(2)
	except:
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #登陆状态则回到热门页面
		sleep(2)
		
		
def init_logout(self):
	#处理已登录需要退出登录情况
	sleep(5)
	self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my_lay').click() #点击底导上的我
	try:
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/fans_layout').click()
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()#点击返回
		sleep(2)
		self.driver.swipe(600,1000,600,200)
		sleep(2)
		self.driver.swipe(600,1000,600,200)
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/setting_layout').click()#点击设置
		sleep(2)
		self.driver.swipe(600,1000,600,200)
		sleep(2)
		self.driver.swipe(600,1000,600,200)
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/logout_button').click()#点击退出登录
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/dialog_right_buton').click()#点击确定
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()#点击返回
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #登陆状态则回到热门页面
		sleep(2)
	except:
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #登陆状态则回到热门页面
		sleep(2)
		
		