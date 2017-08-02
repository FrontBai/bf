#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# qiubai.py

import urllib
import urllib2
import re
import sys
import thread
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class QBspider(object):
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		self.headers = {'User-Agent' : self.user_agent}
		self.stories = []	#存放段子的变量，每一个元素是每一页的段子
		self.enable = False

	def getPage(self, pageIndex):
		
		try:
			url = 'http://www.qiushibaike.com/hot/page' + str(pageIndex)
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode
			#print content
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print "failed to connect qiushibaike, failed reason: ", e.reason
				return None
	
	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print "failed to load page..."
			return None
		pattern = re.compile(r'<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?content.>.*?<span>(.*?)</span>.*?<!--.*?gif -->(.*?)<div class=\"stats\">.*?<span.*?stats-vote.*?number\">(\d+?)</i>.*?<a href=.*?web-list-comment.*?>.*?<i class=\"number\">(\d+?)</i>', re.S)
		items = re.finditer(pattern, pageCode)
		pageStories = []
		for item in items:
			haveImg = re.search("img", item.group(3))
			if not haveImg:
				pageStories.append([item.group(1), item.group(2), item.group(4), item.group(5)])
		return pageStories
	
	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItems(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1
	def getOneStory(self, pageStories, page):
		for story in pageStories:
			input = raw_input()
			self.loadPage()
			if input == "Q":
				self.enable = False
				return
			print "now page: %d\n author: %s\ncontent:%s\nfunny: %s\tcomment: %s" % (page, story[0], story[1], story[2], story[3])

	def start(self):
		print u"正在读取糗事百科，安回车查看新段子，Q退出"
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories) > 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories, nowPage)

spider = QBspider()
spider.start()
