#! /usr/bin/env python
# -*- coding:utf-8 -*-
# BBS_spider.py
# __author__ = 'Front Bai'
"This is a spider which crawl content from baiduBBS"

import urllib
import urllib2
import re

class BDbbs(object):
	def __init__(self, baseUrl, seeLZ):
		self.baseUrl = baseUrl
		self.seeLZ = '?see_lz=' + str(seeLZ) + '&pn='
	
	def getPage(self, pageNum):
		try:
			url = self.baseUrl + self.seeLZ + str(pageNum)
			print url
			user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.3    6 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
			h = {'User-Agent' : user_agent}
			request = urllib2.Request(url, headers=h)
			response = urllib2.urlopen(request)
			#print response.read()
			return response.read()
		except urllib2.URLError, e:
			if hasattr(e, 'reason'):
				print "connection fail, error:", e.reason
				return None

	def getTitle(self, page):
#		page = self.getPage(1)
		pattern = re.compile(r'<h3 class=\"core_title_txt.*?title=\"(.*?)\".*?</h3>', re.S)
		result = re.search(pattern, page)
		print result
		if result:
			title_result = result.group(1)
			#print title_result
			return title_result.strip()
		else:
			return None

	def getPageNum(self, page):
#		page = self.getPage(1)
		pattern = re.compile(r'<li class=\"l_reply_num".*?<span class=.*?3px\">(\d+)</span>', re.S)
		result = re.search(pattern, page)
		if result:
			result_Num = result.group(1)
			return result_Num.strip()
		else:
			return None

	def getContent(self, page):
		pattern = re.compile(r'<div id=\"post_content.*?j_d_post_content \">(.*?)<img class=.*?src=\"(.*?)\" pic_ext.*?<br>(.*?)</div>', re.S)
		result = re.finditer(pattern, page)
		for item in result:
			print item.group(0), '\n', '\n'
		return None



baseURL = 'http://tieba.baidu.com/p/3138733512'
BBS = BDbbs(baseURL, 1)
page = BBS.getPage(1)
print BBS.getTitle(page), '\n', BBS.getPageNum(page)
BBS.getContent(page)


