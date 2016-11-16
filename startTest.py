#coding:utf-8
#Edit by liyuanhong 2016/10/17#

import unittest
import sys
import os

curDir = sys.path[0]

#windows下的写法
sys.path.append(curDir + '\\MPTestCases\\login')
sys.path.append(curDir + '\\MPTestCases\\shoot')
sys.path.append(curDir + '\\MPTestCases\\settingPage')
sys.path.append(curDir + '\\MPTestCases\\hotPage')
sys.path.append(curDir + '\\MPTestCases\\myPage')
sys.path.append(curDir + '\\MPTestCases\\detailPage')

#mac下的写法
sys.path.append(curDir + '/MPTestCases/login')
sys.path.append(curDir + '/MPTestCases/shoot')
sys.path.append(curDir + '/MPTestCases/settingPage')
sys.path.append(curDir + '/MPTestCases/hotPage')
sys.path.append(curDir + '/MPTestCases/myPage')
sys.path.append(curDir + '/MPTestCases/detailPage')


import MPlogin
import MPshoot
import MPsetting
import MPHotpage
import MPHotpageBanner
import MPmypage
import MPdetailPage
import MPmypageSetUserInfo


#MPlogin.suite("0")
#MPshoot.suite("0")
#MPsetting.suite("0")
#MPHotpage.suite("0")
#MPHotpageBanner.suite("0")
#MPmypage.suite("0")
#MPdetailPage.suite("0")
MPmypageSetUserInfo.suite("0")
