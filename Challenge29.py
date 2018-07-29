#-*- coding: utf-8 -*-
import codecs
import sys

import requests

import CookieManager


challengeUrl = "http://webhacking.kr/challenge/web/web-14"

uploadFile = {
    "upfile": open("Challenge21.py")
}

sessionCookie = {
    "PHPSESSID": "a51840b57e5b3e4fb1af134b4054c3a1"
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