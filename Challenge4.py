#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager
import base64


challengeUrl = "http://webhacking.kr/challenge/web/web-04/index.php"
sessionId = "d106ebfb4bba898681f92c7f5316fa6b"


CookieManager.addCookie("PHPSESSID", sessionId)

base64Text = "YzQwMzNiZmY5NGI1NjdhMTkwZTMzZmFhNTUxZjQxMWNhZWY0NDRmMg=="

print "[*] Decode Base64 Text"
decodedBase64 = base64.decodestring(base64Text)
print "[+] ", decodedBase64

print "[*] Crack SHA-1 HexString"
print "[+]", decodedBase64
print "[+]", "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
print "[+]", "test"

parameters = urllib.urlencode({
    "key": "test"
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
