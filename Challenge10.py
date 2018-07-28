#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/codeing/code1.html?go=800"
httpRequest = urllib2.Request(challengeUrl)
CookieManager.addCookie("PHPSESSID", "79d2e02ad592877ec33fb8651960469d")
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.add_header("Referer", "http://webhacking.kr/challenge/codeing/code1.html")

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
