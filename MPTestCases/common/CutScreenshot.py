#coding:utf-8
#Edit by liyuanhong 2016/10/19#
import os
import sys
import platform

def cutScreenShot(self,picName):
	if(platform.system() == "Darwin"):
		filePath = os.getcwd()
	elif(platform.system() == "Windows"):
		filePath = os.path.split(os.path.realpath(sys.argv[0]))[0]  #获取当前脚本路径
	else:
		filePath = os.path.split(os.path.realpath(sys.argv[0]))[0]  #获取当前脚本路径

		
	if(platform.system() == "Darwin"):
		fileName = filePath + "/errorScreenShot/" + picName + ".png"  #将用例方法名作为图片名
	elif(platform.system() == "Windows"):
		fileName = filePath + "\\errorScreenShot\\" + picName + ".png"  #将用例方法名作为图片名
	else:
		fileName = filePath + "\\errorScreenShot\\" + picName + ".png"  #将用例方法名作为图片名
	self.driver.get_screenshot_as_file(fileName)
	print x #让该条用例执行失败
	print traceback.format_exc()
	sleep(2)

