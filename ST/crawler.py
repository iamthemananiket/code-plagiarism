import json
from pprint import pprint
import urllib
import os.path
import urllib2
from bs4 import BeautifulSoup
import HTMLParser
import re
import requests
import sys
import time
url = "https://www.codechef.com/submissions"
values = {
	"sort_by": "All",
	"sorting_order": "asc",
	"status": "15",
	"language": "",
	"year": "",
	"Submit": "GO",
	"handle": ""
}
def makeRequest(url):
	done = False
	i = 0
	the_page = None
	while not done:
		try:
			req = urllib2.Request(url)
			# print(data, url, handle, urllib2.urlopen(req).geturl())
			response = urllib2.urlopen(req)
			the_page = response.read()
		except:
			print(i, handle)
			time.sleep(i)
			i = i + 2
		if the_page:
			print(url, len(the_page))
			done = True
		else:
			print(url)
	return the_page

h = HTMLParser.HTMLParser()
with open("users.json") as f:
	config = json.load(f)
	for handle in config['handle']:
		values['handle'] = handle
		if handle != "fataleagle":
			continue
		for year in config['year']:
			values['year'] = year
			for language in config["language"]:
				values['language'] = language
				data = urllib.urlencode(values)
				the_page = makeRequest(url + "?" + data)

				soup = BeautifulSoup(the_page, 'html.parser')
				for tr in soup.findAll('tr', class_='\\"kol\\"'):
					trList = list(tr)
					try:
						href, pCode = trList[-1].find("a")["href"], trList[3].find("a")["title"]
						if href.find("/viewsolution/") >= 0:
							href = "https://www.codechef.com"+href.replace("viewsolution", "viewplaintext")
						# print(pCode, handle, href)
						code_page = makeRequest(href)
						code = BeautifulSoup(code_page).get_text()
						code = h.unescape(code)
						# print(len(code), code)
						fileName = handle+"_"+pCode+"_"+language
						if not os.path.isfile(fileName):
							f = open(fileName, "w")
							f.write(code)
							f.close()
					except Exception as e:
						# sprint sys.exc_info()
						pass
				time.sleep(2)
					# for element in td:
					# 	print(element)
				# try:
				# 	href = a['href']
				# 	if href.find("/viewsolution/") >= 0:
				# 		print("https://www.codechef.com"+href.replace("viewsolution", "viewplaintext"))
				# except:
				# 	pass
				# print(the_page)
				# break