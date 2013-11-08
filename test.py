#!/usr/local/bin/python

try:
	print "try process"
	with open('/home/bwareham/output/vaticanSearchStringTEST.txt', 'r') as sentFile:
		print "SearchString process" #TEST
		print sentFile.read()
		searchString = sentFile.read()
		print searchString
		print "searchString success"
except:
	print "exception"