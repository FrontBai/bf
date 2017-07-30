#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# qiubai.py

import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

page = 1
url = 'http://www.qiushibaike.com/hot/page' + str(page)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	#print content
	#pattern = re.compile(r'<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?conten.>.*?<span>(.*?)</span>.*?<(img.*?src=.*?)</a>.*?<span.*?stats-vote.><.*?number.>(\d+?)<.*?<.*?web-list-comment.*?>.*?<i.*?number.>(\d+?)</i>', re.S)
	pattern = re.compile(r'<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?content.>.*?<span>(.*?)</span>.*?<!--.*?gif -->(.*?)<div.*?stats.>', re.S)
	items = re.findall(pattern, content)
	print items
	for j in items:
		print j
	#for item in items:
	#	for i in item:
	#		print i
	#for item in items:
	#	haveImg = re.search("img", item[2])
	#	if not haveImg:
	#		print item[0], item[1], item[2], item[3], item[4]
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
