# usage: python2 sendcookie.py
# simulates a legitimate user logging in

import cookielib
import urllib2

# Create a MozillaCookieJar to hold the cookies
cookie_jar = cookielib.MozillaCookieJar()

# Load the saved cookies into the CookieJar
# Assuming cookies are stored in a file named 'cookies.txt'
cookie_file = 'cookies.txt'
cookie_jar.load(cookie_file, ignore_discard=True, ignore_expires=True)

# Create a handler to manage the cookies
cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)

# Build an opener with the cookie handler
opener = urllib2.build_opener(cookie_handler)

# Make a request using the opener
url = 'https://www.heartbleedlabelgg.com/messages/inbox/admin'
headers = {
	'REQUEST': '/messages/inbox/admin HTTP/1.1',	
	'Host': 'www.heartbleedlabelgg.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0',
	'Accept': 'text/html',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'https://www.heartbleedlabelgg.com/messages/add/33',
	'Cookie': 'Elgg=jngj1a11v2jhh02vc7amb4eim1; PHPSESSID=f9kopkgr073nbjhuifd6sssgf4',
	'Connection': 'keep-alive',
}

request = urllib2.Request(url, headers=headers)
response = opener.open(request)

# Now, you can process the response as needed
print(response.read())
