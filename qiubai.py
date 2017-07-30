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
	pattern = re.compile(r'<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?content.>.*?<span>(.*?)</span>.*?<!--.*?gif -->(.*?)<div class=\"stats\">.*?<span.*?stats-vote.*?number\">(\d+?)</i>.*?<a href=.*?web-list-comment.*?>.*?<i class=\"number\">(\d+?)</i>', re.S)
	items = re.finditer(pattern, content)
	#print items
	#for j in items:
	#	print j.group(3)
	for item in items:
		haveImg = re.search("img", item.group(3))
		if not haveImg:
			print item.group(1), item.group(2), "funny: "+item.group(4), "comment: "+item.group(5)
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
