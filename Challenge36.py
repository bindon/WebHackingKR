#-*- coding: utf-8 -*-
import urllib2
import CookieManager
httpConnection = None

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-8/.index.php.swp"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
httpRequest = urllib2.Request(challengeUrl)
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
