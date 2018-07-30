#-*- coding: utf-8 -*-
import base64
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-20/"
print "[!] Download and Cracking zip file"
print "[*]", challengeUrl + "?down=" + base64.encodestring("test.zip")

print "[*] Get Password"
challengeUrl = "http://webhacking.kr/challenge/web/web-20/good.html"
CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")
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

print "[*] Auth"
challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "123456789null0987654321"
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
