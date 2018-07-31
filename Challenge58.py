#-*- coding: utf-8 -*-
import urllib2

import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-35/g1v2m2passw0rd.php"

print "[*] Clear Challenge 58"
CookieManager.addCookie("PHPSESSID", "e52509baa15ced3a5be56d2efc0239b6")

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
