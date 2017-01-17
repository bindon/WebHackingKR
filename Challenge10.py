#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/codeing/code1.html?go=800"
httpRequest = urllib2.Request(challengeUrl)
CookieManager.addCookie("PHPSESSID=da0bd6cb852292c17cc2364c9dc6d334") # webhacking.kr에 로그인 하고 나온 cookie
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.add_header("Referer", "http://webhacking.kr/challenge/codeing/code1.html")
httpRequest.get_method = lambda: 'GET'

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
