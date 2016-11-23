#coding:utf-8
'''
Created on 2016年11月日
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

class MPRewardPage(unittest.TestCase):
    def __init__(self,methodName):
        unittest.TestCase.__init__(self, methodName)
        print '************************** MPRewardPage test **************************'
    #初始化操作
    def setUp(self):
        Initialize.setUp(self)

    #测试用例执行完成后的操作
    def tearDown(self):
        Initialize.tearDown(self)
        '''
        1、打开秒拍，进入发现页面
        2、切换到悬赏tab页面
        3、点击任意一个悬赏的用户头像，进入个人主页
        4、点击返回
        5、点击悬赏描述，进入悬赏详情页面
        6、点击返回
        7、点击悬赏视频缩略图，进入悬赏详情页面
        8、点击更多悬赏
        9、点击返回到悬赏详情
        10、点击悬赏金额，弹出悬赏描述，点击关闭按钮
        11、点击悬赏金额，弹出悬赏描述
        12、点击确定按钮
        13、点击右上角的分享按钮
        14、点击分享到微博？？？
        15、点击右上角的分享按钮，点击复制链接
        16、来回切换排行和全部
        17、全部页面上拉加载一次
        18、悬赏页面下拉刷新
        19、点击发布新悬赏
        20、点击关闭按钮
        21、点击拍视频领取奖金
        22、点击返回按钮
        23、点击返回到发现页面
        24、点击首页，回到首页
        '''
    def test_Rewardpaage(self):
        try:
            print 'start test_Rewardpaage test ...  '
            Initialize.init_case(self)  #处理开屏广告是否存在的情况
            sleep(5)
            InitLogin.init_logout(self)
            sleep(5)
            InitLogin.init_login(self)
            sleep(5)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_message_lay').click()#点击发现
            sleep(6)
            self.driver.find_element_by_xpath('//android.widget.HorizontalScrollView[contains(@id,com.yixia.videoeditor:id/find_headview_tabs)]/android.widget.LinearLayout[1]').click()#点击悬赏
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/icon').click()#点击头像
            sleep(2)
            self.driver.keyevent('4')#点击返回
            sleep(2)
            self.driver.swipe(500,1000,500,200)
            sleep(2)
            self.driver.find_element_by_xpath('//android.widget.ListView[contains(@id,android:id/list)]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[contains(@id,com.yixia.videoeditor:id/user_layout)]/android.widget.TextView[contains(@id,com.yixia.videoeditor:id/desc)]').click()#点击描述进入悬赏详情
            sleep(2)
            self.driver.keyevent('4')#点击返回
            sleep(2)
            self.driver.find_element_by_xpath('//android.widget.ListView[contains(@id,android:id/list)]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[contains(@id,com.yixia.videoeditor:id/bounty_title2)]/android.widget.LinearLayout/android.widget.RelativeLayout[contains(@id,com.yixia.videoeditor:id/top1_layout)]').click()#点击缩略图进入悬赏详情
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/headview_about').click()#点击更多悬赏
            sleep(2)
            self.driver.keyevent('4')#点击返回
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/headview_bounty').click()#点击金额
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()#点击关闭
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/headview_bounty').click()#点击金额
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/agree_view').click()#点击确定
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleRight').click()#点击分享
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/sina_weibo').click()#点击微博
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/share_sinaweibo_dialog_close').click()#点击关闭
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleRight').click()#点击分享
            sleep(2)
            width=self.driver.get_window_size().get('width')
            height=self.driver.get_window_size().get('height')
            #print width
            #print height
            x_start=900*width/1080
            x_end=130*width/1080
            y=1500*height/1920
            self.driver.swipe(x_start,y,x_end,y)
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/copy_url').click()#点击复制链接
            sleep(2)
            self.driver.swipe(500,300,500,1000)#下拉加载
            sleep(2)
            self.driver.swipe(500,1300*height/1920,500,500*height/1920)
            sleep(2)
            self.driver.find_element_by_xpath('//android.widget.HorizontalScrollView[contains(@id,com.yixia.videoeditor:id/tabs)]/android.widget.LinearLayout[1]').click()#切换全部
            sleep(2)
            self.driver.swipe(500,1300*height/1920,500,500*height/1920)
            sleep(2)
            self.driver.swipe(500,1300*height/1920,500,500*height/1920)
            sleep(2)
            self.driver.swipe(500,1300*height/1920,500,500*height/1920)
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/new_reward').click()#点击发布新悬赏
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/titleLeft').click()#点击关闭
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/getbonus_reward').click()#点击拍摄领取奖金
            sleep(2)
            self.driver.keyevent('4')#点击返回
            sleep(2)
            self.driver.keyevent('4')#点击返回
            sleep(2)
            self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_feed').click()
            sleep(2)
            
        except Exception,e:
            print traceback.format_exc()
            CutScreenshot.cutScreenShot(self,sys._getframe().f_code.co_name)
            
def suite(self):
    suite = unittest.TestSuite()  
    suite.addTest(MPRewardPage('test_Rewardpaage'))  

    runner = unittest.TextTestRunner()  
    runner.run(suite)

        
