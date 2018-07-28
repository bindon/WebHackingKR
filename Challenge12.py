#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/codeing/code3.html"
httpRequest = urllib2.Request(challengeUrl + "?" + urllib.quote("=youaregod~~~~~~~!"))
CookieManager.addCookie("PHPSESSID", "79d2e02ad592877ec33fb8651960469d")
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
