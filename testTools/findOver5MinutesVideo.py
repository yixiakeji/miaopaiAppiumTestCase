#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('gbk')

import urllib
import json
from time import sleep
import types
import time

#根据suid获取用户名
def getUserName(suid):
	userName = ""
	#params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':'Z1fV~4uV6WRqfs3xndogdA__','version': '6.6.0.1','per':20})
	params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':suid,'version': '6.6.0.1','per':20})
	dat = urllib.urlopen("http://api.miaopai.com/m/space_user_info.json?%s" % params)
	jdat = json.loads(dat.read())
	userName = jdat['result']['header']['nick']
	#print userName
	return userName

#将以毫秒为单位的时间戳转换为日期格式
def convertToDate(timestamp):
	#theTime = jdat['result'][i]['channel']['ext']['finishTime']
	theDate = str(timestamp)[:-3]
	timeArray = time.localtime(int(theDate))
	otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	return otherStyleTime


#找首页频道超过5分钟的视频*****************************************
def testFenlei():
	categorys = [114]
	theMax = 0
	thecount = 1
	for cat in categorys:
		for var in range(1,2000):
			#首页各个频道
			params = urllib.urlencode({'cateid': cat, 'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
			dat = urllib.urlopen("http://api.miaopai.com/m/cate2_channel.json?%s" % params)
			jdat = json.loads(dat.read())
			#it = jdat['per']
			it = len(jdat['result'])
			for i in range(0,it):
				judge = jdat['result'][i].has_key('color')
				if judge:
					pass
				else:
					theTime = jdat['result'][i]['channel']['ext']['length']
					#print theTime
					if theTime > theMax:
						theMax = theTime
					if theTime >= 300:
						print "channel : " + jdat['name'] + "第 " + str(var) + "页"
						print "时长 : " + str(theTime) + " 秒"
						print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
						print "time : " + jdat['result'][i]['channel']['ext']['finishTimeNice']
						print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
						try:
							print "t : " + jdat['result'][i]['channel']['ext']['t']
							print "ft : " + jdat['result'][i]['channel']['ext']['ft']
						except:
							print "t和ft字段包含特殊字符"
						print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
						print "***********************************************"
						print ""
					else:
						print str(thecount) + "  --  this video is less than 300 seconds !"
					thecount = thecount + 1
			sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#找热门超过5分钟的视频****************************************
def testHot():
	theMax = 0
	thecount = 1
	for var in range(1,2000):
		#首页热门
		params = urllib.urlencode({'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v6_hot_channel.json?%s" % params)
		jdat = json.loads(dat.read())
		#it = jdat['per']
		it = len(jdat['result'])
		for i in range(0,it):
			judge = jdat['result'][i].has_key('color')
			if judge:
				pass
			else:
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "channel : " + "热门" + "第 " + str(var) + "页"
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					try:
						print "t : " + jdat['result'][i]['channel']['ext']['t']
						print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					except:
						print "t和ft字段存在特殊编码"
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#找个人主页超过5分钟的视频***************************************
def testMyPage(suid):
	theMax = 0
	timeflag = 0
	page = 1
	thecount = 1
	while(int(timeflag) != -1):
		#print timeflag
		#params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':'Z1fV~4uV6WRqfs3xndogdA__','version': '6.6.0.1','timeflag':timeflag,'per':20})
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','suid':suid,'version': '6.6.0.1','timeflag':timeflag,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/channel_forward_reward.json?%s" % params)
		jdat = json.loads(dat.read())
		timeflagOld = timeflag
		timeflag = jdat['result']['timeflag']
		it = jdat['result']['stream']['cnt']

		it = int(jdat['result']['stream']['cnt'])
		for i in range(0,it):
			judge = jdat['result']['stream']['list'][i].has_key('channel')
			#print judge
			if not judge:
				pass
			else:
				theTime = jdat['result']['stream']['list'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print getUserName(suid) + "第 " + str(page) + "页"
					print 'timeFlag : ' + str(timeflagOld)
					#print 'timeFlag : ' + str(jdat['result']['timeflag'])
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result']['stream']['list'][i]['channel']['stream']['base'] + ".mp4"
					print "time : " + jdat['result']['stream']['list'][i]['channel']['ext']['finishTimeNice']
					print "t : " + jdat['result']['stream']['list'][i]['channel']['ext']['t']
					print "ft : " + jdat['result']['stream']['list'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result']['stream']['list'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		page = page + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax



#找悬赏列表超过5分钟的视频***************************************
def testRewordList(srwid):
	theMax = 0
	page = 1
	thecount = 1
	rewordId = 0
	pageIndex = 1
	while True:
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','filter':'all','version': '6.6.0.1','srwid':srwid,'pageIndex':pageIndex,'pageSize':10})
		dat = urllib.urlopen("http://api.miaopai.com/m/getRewardVideos.json?%s" % params)
		jdat = json.loads(dat.read())
		videos = len(jdat['result']['list'])
		if(videos == 0):
			break
		else:
			#print "continue"
			it = jdat['result']['listSize']
			for i in range(0,videos):
				theTime = jdat['result']['list'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "第 : " + str(pageIndex) + "页"
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result']['list'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result']['list'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result']['list'][i]['channel']['ext']['owner']['nick']
					try:
						print "t : " + jdat['result']['list'][i]['channel']['ext']['t']
					except:
						print "t字段有特殊字符"
					try:
						print "ft : " + jdat['result']['list'][i]['channel']['ext']['ft']
					except:
						print "ft字段有特殊字符"
					print "pic : " + jdat['result']['list'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
			pageIndex = pageIndex + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#合集页面视频时长测试***************************************
def testVideoColloctions(stpid):
	theMax = 0
	page = 1
	thecount = 1
	while True:
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','type':'0','version': '6.6.0.1','stpid':stpid,'page':page,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v2_topic.json?%s" % params)
		jdat = json.loads(dat.read())
		videos = len(jdat['result'])
		if(videos == 0):
			break
		else:
			#print "continue"
			it = jdat['per']
			for i in range(0,videos):
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "第 : " + str(page) + "页"
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					print "t : " + jdat['result'][i]['channel']['ext']['t']
					print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
			page = page + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax



#话题页面视频时长测试***************************************
def testTopic(topicname):
	theMax = 0
	page = 1
	thecount = 1
	while True:
		params = urllib.urlencode({'token': 'u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL','type':'2','version': '6.6.0.1','topicname':topicname,'page':page,'per':20})
		dat = urllib.urlopen("http://api.miaopai.com/m/v2_topic.json?%s" % params)
		jdat = json.loads(dat.read())
		videos = len(jdat['result'])
		if(videos == 0):
			break
		else:
			#print "continue"
			it = jdat['per']
			for i in range(0,videos):
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "第 : " + str(page) + "页"
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					theTime = jdat['result'][i]['channel']['ext']['finishTime']
					theDate = convertToDate(theTime)
					print "time : " + theDate
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					print "t : " + jdat['result'][i]['channel']['ext']['t']
					print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
			page = page + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax


#找同城超过5分钟的视频*****************************************
def testSameCity(orderby):
	theMax = 0
	thecount = 1
	for var in range(1,10):
		#首页各个频道
		params = urllib.urlencode({'token': 'OIynN5UcxhH082kWvIw7YWP4CTHYSeKI', 'version': '6.6.0.1','page': var,'per':20,'orderby':orderby})
		dat = urllib.urlopen("http://api.miaopai.com/m/samecity_v6.json?%s" % params)
		jdat = json.loads(dat.read())
		it = jdat['per']
		for i in range(0,it):
			judge = jdat['result'][i].has_key('color')
			if judge:
				pass
			else:
				theTime = jdat['result'][i]['channel']['ext']['length']
				#print theTime
				if theTime > theMax:
					theMax = theTime
				if theTime >= 300:
					print "同城 : " + "第 " + str(var) + "页"
					print "时长 : " + str(theTime) + " 秒"
					print "url : " + jdat['result'][i]['channel']['stream']['base'] + ".mp4"
					print "time : " + jdat['result'][i]['channel']['ext']['finishTimeNice']
					print "userName : " + jdat['result'][i]['channel']['ext']['owner']['nick']
					try:
						print "t : " + jdat['result'][i]['channel']['ext']['t']
						print "ft : " + jdat['result'][i]['channel']['ext']['ft']
					except:
						print "f和ft字段包含特殊字符"
					print "pic : " + jdat['result'][i]['channel']['pic']['base'] + ".jpg"
					print "***********************************************"
					print ""
				else:
					print str(thecount) + "  --  this video is less than 300 seconds !"
				thecount = thecount + 1
		sleep(2)
	print ""
	print ""
	print ""
	print "the max is : "
	print theMax







#------------------------------------------
#testFenlei()   #频道分类测试

#------------------------------------------
#testHot()       #首页热门

#------------------------------------------
#suid = 'Z1fV~4uV6WRqfs3xndogdA__'   #凡益网趣的suid
#suid = 'SBr3gTpwGbI53Lhyuz4xCg__'   #yiixia24000v的suid
#suid = 'AkwnpO4BXM4~G5BN' #远洪88的suid
#suid = 'muQzRaQTXu5dFPbf'
#testMyPage(suid)       #个人页面

#-------------------------------------------
#srwid = 'XrEmnRLbfqQ_'    
#testRewordList(srwid)       #悬赏页面

#-------------------------------------------
stpid = 'wOMjeIvel9HFcvUi'    
testVideoColloctions(stpid)    #合集页面

#-------------------------------------------
#topicname = '半月朋友'    
#testTopic(topicname)              #话题页面

#-------------------------------------------
#orderby = 'bscore'    #颜值
#orderby = 'hot'    #热度
#testSameCity(orderby)   #同城页面那











########################################################################################################################################
#http://api.miaopai.com/m/v6_hot_channel.json?token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&refresh=3&version=6.6.0.1&page=2&per=20   #热门接口
#http://api.miaopai.com/m/cate2_channel.json?cateid=128&token=OIynN5UcxhH082kWvIw7YWP4CTHYSeKI&version=6.6.0.1&page=1&per=20   #频道接口
#http://api.miaopai.com/m/channel_forward_reward.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&suid=Z1fV~4uV6WRqfs3xndogdA__&version=6.6.0.1&timeflag=1475982730748&per=20 #个人主页
#http://api.miaopai.com/m/space_user_info.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&version=6.6.0.1&suid=Z1fV~4uV6WRqfs3xndogdA__  #个人页面个人信息
#http://api.miaopai.com/m/getRewardVideos.json?filter=all&srwid=0v8jWapHanpBaPhk&token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&pageSize=10&pageIndex=1&version=6.6.0.1  #悬赏全部视频列表

#合集与话题的区别在于合集有（type=0,stpid,topicname）话题有（type=2,topicname）;话题缺少topicname参数无法获取数据
#http://api.miaopai.com/m/v2_topic.json?topicname=%E7%8E%8B%E5%AE%9D%E5%BC%BA%E6%8C%87%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8&token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&version=6.6.0.1&page=1&type=0&per=20&stpid=GNIlmdwJfZyvWMqt  #视频合集王宝强指责妻子出轨
#http://api.miaopai.com/m/v2_topic.json?topicname=%E7%8E%8B%E5%AE%9D%E5%BC%BA%E6%8C%87%E5%A6%BB%E5%AD%90%E5%87%BA%E8%BD%A8&token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&version=6.6.0.1&page=1&type=2&per=20  #话题王宝强指责妻子出轨
#http://api.miaopai.com/m/samecity_v6.json?token=u~p36u0UjaIvJwxYJpp1wkGdbdeX7LbL&orderby=bscore&version=6.6.0.1&page=1&per=20  #同城测试


#悬赏列表 ---- 可测试 ----  有方法
#关注页面 ---- 可测试 ----  有方法
#同城页面 ---- 可测试 
#话题页面 ---- 可测试 ----  有方法
#悬赏页面 ---- 可测试 ----  有方法
#视频合集 ---- 可测试
#搜索页面 ---- 可测试 ----  有方法
#个人主页 ---- 可测试 ----  ok
#热榜页面 ---- 可测试 ----  ok（最后一个视频都不在8月1号之前）
#频道分类页面 
#发现页面 ---- 排除（只包含话题和合集）
#频道达人视频封面 ----  可测试 ----  有方法（后台配置一个大于5分钟的视频）



