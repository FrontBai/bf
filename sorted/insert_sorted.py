#! /usr/bin/env python
# -*- coning = utf-8 -*-
# insert_sorted.py

def insert_sorted(alist):
	length = len(alist)
	for i in range(1, length):
		t = alist[i]
		j = i - 1
		while j >= 0:
			if alist[j] > t:
				alist[j+1] = alist[j]
				alist[j] = t
			j -=1
	return alist

a = [12, 2, 14, 15, 6, 1, 6, 33, 45, 66, 7, 88, 1]
b = sorted(a)
print a, '\n', b
print "%s" % (a is b)
print "%s" % (a == b)
c = insert_sorted(a)
print a, '\n', c
print "%s" % (a is c)
print "%s" % (a == c)
