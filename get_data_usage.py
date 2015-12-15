from bs4 import BeautifulSoup
import urllib2

MASTER_URL = "http://www.airtel.in/smartbyte-s/page.html"

landing_page = urllib2.urlopen(MASTER_URL)
for tags in BeautifulSoup(landing_page.read()).findAll('iframe'):
	URL = tags['src']

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open(URL)
page = response.read()
soup = BeautifulSoup(page, "lxml")

count = 1

for info in soup.find_all('span'):
	count = count + 1
	if count == 9:
		print("Current Plan: " + info.string)
	if count == 10:
		print("Topup: " + info.string)
	if count == 11:
		print("Remaining: " + info.string)
	if count == 12:
		print("Remaining days: " + info.string)
	if count == 13:
		print("Subscriber ID: " + info.string) 
