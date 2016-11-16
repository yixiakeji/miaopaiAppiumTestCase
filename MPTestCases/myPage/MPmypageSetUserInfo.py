#coding:utf-8
#Edit by liyuanhong 2016/11/10#

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

class MPmypageSetUserInfo(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self, methodName)
        print "************************** MPmypageSetUserInfo test **************************"
        
    #初始化操作
    def setUp(self):
        Initialize.setUp(self)

    #测试用例执行完成后的操作
    def tearDown(self):
        Initialize.tearDown(self)
    
    #测试各种方式进入个人信息设置页面
    def test_click_into_set_userinfo_page(self):
        try:
            print 'start test_click_into_set_userinfo_page test ...  '
            Initialize.init_case(self)  #处理开屏广告是否存在的情况
            InitLogin.init_login(self)  #如果没有登陆则登陆秒拍
            sleep(5)
            
            self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click()  #点击底导上的我进入我的页面
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/user_info_layout').click()  #点击整条用户信息进入个人页面
            sleep(4)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/text_info').click() #点击用户名和用户描述进入编辑个人资料页面
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click() #编辑个人资料页面点击返回到个人主页
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/edit_icon').click() #点击右箭头进入编辑个人资料页面
            sleep(1)
            self.driver.press_keycode('4')  #击返回按钮回到个人主页
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()  #点击返回到我的页面
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click()  #点击回到热门页面
            sleep(2)
        except Exception,e:
            print traceback.format_exc()
            CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
            
    #测试我的页面修改个人资料的各种操作
    def test_do_change_userinfo_operations(self):
        try:
            print 'start test_do_change_userinfo_operations test ...  '
            Initialize.init_case(self)  #处理开屏广告是否存在的情况
            InitLogin.init_login(self)  #如果没有登陆则登陆秒拍
            sleep(5)
            
            self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click()  #点击底导上的我进入我的页面
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/user_info_layout').click()  #点击整条用户信息进入个人页面
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/text_info').click() #点击用户名和用户描述进入编辑个人资料页面
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/icon_header').click() #点击修改头像
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/reset_capture').click() #点击拍照上传
            sleep(3)
            self.driver.press_keycode('4')  #击返回按钮回到编辑个人资料页面
            sleep(2)
            
            self.driver.find_element_by_id('com.yixia.videoeditor:id/icon_header').click() #点击修改头像
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/reset_abum').click() #点击手机相册
            sleep(3)
            self.driver.press_keycode('4')  #击返回按钮回到编辑个人资料页面
            sleep(1)
            
            self.driver.find_element_by_id('com.yixia.videoeditor:id/icon_header').click() #点击修改头像
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/remove_cancel').click() #点击取消
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleRightTextView').click() #点击完成，回到我的个人页面
            sleep(1)
            
            self.driver.find_element_by_id('com.yixia.videoeditor:id/text_info').click() #点击用户名和用户描述进入编辑个人资料页面
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/tv_username').click() #点击昵称输入框
            sleep(1)
            self.driver.keyevent(8) #输入1
            sleep(0.5)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/girl_checktv').click() #点击性别女
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/boy_checktv').click() #点击性别男
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/profile_address_layout').click() #点击所在地弹出地址选择框
            sleep(1)
            e1 = self.driver.find_element_by_id('com.yixia.videoeditor:id/regions')  #获取省份选择框
            e2 = self.driver.find_element_by_id('com.yixia.videoeditor:id/city')  #获取城市选择框
            
            e1x1=int (e1.location.get('x')+10)
            e1y1=int (e1.location.get('y')+10)
            e1x2=int (e1.location.get('x')+10)
            e1y2=int (e1.location.get('y')+200)
            
            e2x1=int (e2.location.get('x')+10)
            e2y1=int (e2.location.get('y')+10)
            e2x2=int (e2.location.get('x')+10)
            e2y2=int (e2.location.get('y')+200)
            
            self.driver.swipe(e1x2,e1y2,e1x1,e1y1,1000) #向上滑动选择省份
            sleep(1)
            self.driver.swipe(e2x2,e2y2,e2x1,e2y1,1000) #向上滑动选择城市
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/cancel_button_select_city').click() #点击取消按钮
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/profile_address_layout').click() #点击所在地弹出地址选择框
            sleep(1)
            self.driver.swipe(e1x2,e1y2,e1x1,e1y1,1000) #向上滑动选择省份
            sleep(1)
            self.driver.swipe(e2x2,e2y2,e2x1,e2y1,1000) #向上滑动选择城市
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/ok_button_select_city').click() #点击确定按钮
            sleep(1)
            
            e3 = self.driver.find_element_by_id('com.yixia.videoeditor:id/edt_sign') #获取个性签名元素
            e3.click()  #点击手机号输入框弹出键盘
            sleep(0.5)
            e3.send_keys('aaaaaaa')
            sleep(1)
            self.driver.press_keycode('4')  #击返回收起键盘
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleRightTextView').click() #点击完成，回到我的个人页面
            sleep(3)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click() #点击返回到我的页面
            sleep(1)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click() #点击首页回到首页
            sleep(1)
            
            
            
        except Exception,e:
            print traceback.format_exc()
            CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
    
def suite(self):
    suite = unittest.TestSuite()  
    #测试意见反馈功能
    suite.addTest(MPmypageSetUserInfo('test_click_into_set_userinfo_page'))
    suite.addTest(MPmypageSetUserInfo('test_do_change_userinfo_operations'))

    runner = unittest.TextTestRunner()  
    runner.run(suite)
    
    
    
    
    
    
    