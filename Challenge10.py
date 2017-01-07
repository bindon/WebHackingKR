#-*- coding: utf-8 -*-
import urllib2
import CookieConstants

challengeUrl = "http://webhacking.kr/challenge/codeing/code1.html?go=800"
httpRequest = urllib2.Request(challengeUrl)
httpRequest.add_header("Cookie", CookieConstants.sessionId)
httpRequest.add_header("Referer", "http://webhacking.kr/challenge/codeing/code1.html")
httpRequest.get_method = lambda: 'GET'

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
