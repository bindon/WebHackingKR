#-*- coding: utf-8 -*-
import urllib
import urllib2
import hashlib
import CookieManager
import time
httpConnection = None

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/?get=hehe"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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

# Level 2
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/lv2.php"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")

parameters = urllib.urlencode({
    "post": "hehe", 
    "post2": "hehe2"
})

httpRequest = urllib2.Request(challengeUrl, data=parameters)
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

# Level 3
ipAddress = ""
httpConnection = None
print "[+] Find IP Address"
try:
    httpRequest = urllib2.Request("https://api.ipify.org")
    httpConnection = urllib2.urlopen(httpRequest)
    ipAddress = httpConnection.read()
    print "[*] Your IP Address is [", ipAddress, "]"
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/33.php?myip=" + ipAddress
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")

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

# Level 4
parameter = hashlib.md5(str(int(time.time()+4))).hexdigest()
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/l4.php?password=" + parameter
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")

httpRequest = urllib2.Request(challengeUrl)
httpRequest.add_header("Cookie", CookieManager.getCookie())

httpConnection = None

try:
    for idx in range(0, 5):
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        if httpResponse.find('Next') > 0:
            print httpResponse
            break
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()
# Level 5
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/md555.php?imget=1"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
CookieManager.addCookie("imcookie", "1")
parameter = urllib.urlencode({
    "impost": "1"
})

httpRequest = urllib2.Request(challengeUrl, data=parameter)
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.get_method = lambda: "POST"
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

# Level 6
ipAddress = ""
httpConnection = None
print "[+] Find IP Address"
try:
    httpRequest = urllib2.Request("https://api.ipify.org")
    httpConnection = urllib2.urlopen(httpRequest)
    ipAddress = httpConnection.read()
    print "[*] Your IP Address is [", ipAddress, "]"
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

hashedIpAddress = hashlib.md5(ipAddress).hexdigest()
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/gpcc.php"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
CookieManager.addCookie("test", hashedIpAddress)
parameter = urllib.urlencode({
    "kk": hashedIpAddress
})
httpRequest = urllib2.Request(challengeUrl, data=parameter)
httpRequest.add_header("Cookie", CookieManager.getCookie())
httpRequest.add_header("User-Agent", ipAddress)
httpRequest.get_method = lambda: "POST"
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
# Level 7
ipAddress = ""
httpConnection = None
print "[+] Find IP Address"
try:
    httpRequest = urllib2.Request("https://api.ipify.org")
    httpConnection = urllib2.urlopen(httpRequest)
    ipAddress = httpConnection.read()
    print "[*] Your IP Address is [", ipAddress, "]"
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

ipAddress = ipAddress.replace(".", "")
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/wtff.php?"+ipAddress+"="+ipAddress
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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
# Level 8
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/ipt.php?addr=127.0.0.1"
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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

# Level 9
answer = ""
for idx in range(97, 123, 2):
    answer += chr(idx)
    
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6/nextt.php?ans="+answer
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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

# Level 10
ipAddress = ""
httpConnection = None
print "[+] Find IP Address"
try:
    httpRequest = urllib2.Request("https://api.ipify.org")
    httpConnection = urllib2.urlopen(httpRequest)
    ipAddress = httpConnection.read()
    print "[*] Your IP Address is [", ipAddress, "]"
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

idx = 0
while True:
    if idx > ipAddress.__len__():
        break
    ipAddress = ipAddress.replace(str(idx), str(ord(str(idx)[0])))
    idx += 1

ipAddress = ipAddress.replace(".", "")
ipAddress = ipAddress[0:10]
answer = (str((float(ipAddress))/2)).replace(".", "")

parameter = "/answerip/"+ipAddress+"/"+answer+"."+ipAddress
challengeUrl = "http://webhacking.kr/challenge/bonus/bonus-6" + parameter
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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

# Auth
challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "c7042fc5927e6e4eb85c5821e53faab5"
});
httpRequest = urllib2.Request(challengeUrl, data=parameter)
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
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
