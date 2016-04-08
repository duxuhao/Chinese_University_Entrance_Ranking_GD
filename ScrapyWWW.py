# -*- coding: utf-8 -*-
#import request
import urllib2
from bs4 import BeautifulSoup
import sys

TT = open("UniversityMarksFull.csv","a")
TT.write("University_Name_Location")
TT.write(",")
website = "http://college.gaokao.com/school/tinfo/3/result/14/1/"
req = urllib2.Request(website)
Web = urllib2.urlopen(req)
html = Web.read()
soup = BeautifulSoup(html)
tag = soup.table
th = tag.find('th')
while th:
	TT.write(th.string.encode('utf-8'))
	TT.write(",")
	th = th.findNext('th')
TT.write("Topic")
TT.write("\n")
Topic = ["理科","文科"]
print "Start:"
for i in range(2666):
	for wl in range(2):
		website = "http://college.gaokao.com/school/tinfo/" + str(i+1) + "/result/14/" + str(wl+1) + "/"
		sys.stdout.write(Topic[wl])
		try :
			req = urllib2.Request(website)
			Web = urllib2.urlopen(req)
			html = Web.read()
			soup = BeautifulSoup(html)
			name = soup.h2.string
			print name + " is downloading"
			tag = soup.table
			td = tag.find('td')
			while td:
				TT.write(name.encode('utf-8'))
				TT.write(",")
				for t in range(6):
					if td.string != "------":
						TT.write(td.string.encode('utf-8'))
					td = td.findNext('td')
					TT.write(",")
				TT.write(Topic[wl])
				TT.write("\n")
		except :
			pass


TT.close()
#print(tag.contents)

