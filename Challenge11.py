#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager

ipAddress = ""
httpConnection = None
print "[+] Find IP Address"
try:
    httpRequest = urllib2.Request("https://api.ipify.org")
    httpConnection = urllib2.urlopen(httpRequest)
    ipAddress = httpConnection.read()
    print "Your IP Address is [", ipAddress, "]"
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

print "[*] Try Challenge 11"
challengeUrl = "http://webhacking.kr/challenge/codeing/code2.html" \
    + "?val=" + urllib.quote("3beeef_bindon" + ipAddress + "bindon\tp\ta\ts\ts")
httpRequest = urllib2.Request(challengeUrl)
CookieManager.addCookie("PHPSESSID", "79d2e02ad592877ec33fb8651960469d")
httpRequest.add_header("Cookie", CookieManager.getCookie())

try:
    httpConnection = urllib2.urlopen(httpRequest)
    httpResponse = httpConnection.read()
    print httpResponse
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()
