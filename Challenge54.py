#-*- coding: utf-8 -*-
import urllib
import urllib2
import CookieManager


challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "f105a05dd536eff8a334c453748fc46e"
});
httpRequest = urllib2.Request(challengeUrl, data=parameter)
CookieManager.addCookie("PHPSESSID", "73ea5f35f558006f21f6185c171a2ed9")
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
