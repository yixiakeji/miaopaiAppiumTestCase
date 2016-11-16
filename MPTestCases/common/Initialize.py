#coding:utf-8
#Edit by liyuanhong 2016/10/18#

from appium import webdriver


#测试用例的初始化操作
def init_case(opt):
	#处理开屏广告是否存在的情况
	print "Initialize"
	try:
		sleep(1)
		el = opt.driver.find_element_by_id('com.yixia.videoeditor:id/adver_imageview')   #获取开屏广告是否存在
		opt.driver.find_element_by_id('com.yixia.videoeditor:id/textview')    #点击开屏广告上的'点击跳过'按钮
		sleep(2)
	except Exception,ex:
		pass
		
def setUp(self):
	desired_caps={}
	desired_caps['device']='android'
	desired_caps['platformName']='Android'
	desired_caps['browserName']=''
	desired_caps['version']='6.0.1'
	desired_caps['deviceName']='HUAWEI H60-L01'

	#desired_caps['app'] = PATH('D:\\AndroidAutomation\\AndroidAutoTest\\app\\zhongchou.apk')
	#被测试的App在电脑上的位置
	desired_caps['appPackage']='com.yixia.videoeditor'
	desired_caps['appActivity']='.ui.login.SplashActivity'
	self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
	
def tearDown(self):
	self.driver.quit()
	print 'end ... '
