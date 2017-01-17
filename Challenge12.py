#-*- coding: utf-8 -*-
"""
Web Hacking 12

1. WorkTimeFun의 변수를 확인하면 아래와 같은 내용
===================================================
var enco='';
var enco2=126;
var enco3=33;
var ck=document.URL.substr(document.URL.indexOf('='));
 
 
for(i=1;i<122;i++)
{
enco=enco+String.fromCharCode(i,0);
}
 
function enco_(x)
{
return enco.charCodeAt(x);
}

if(ck=="="+String.fromCharCode(enco_(240))+String.fromCharCode(enco_(220))+String.fromCharCode(enco_(232))+String.fromCharCode(enco_(192))+String.fromCharCode(enco_(226))+String.fromCharCode(enco_(200))+String.fromCharCode(enco_(204))+String.fromCharCode(enco_(222-2))+String.fromCharCode(enco_(198))+"~~~~~~"+String.fromCharCode(enco2)+String.fromCharCode(enco3))
{
alert("Password is "+ck.replace("=",""));
}
===================================================

if문을 보면 "=youaregod~~~~~~~!" 이라는 문자열과 비교하여 확인한다.

그러므로 ck값을 해당 문자열로 맞춰주기 위해 다음 소스코드를 확인
var ck=document.URL.substr(document.URL.indexOf('='));

document.URL의 기본 값은 http://webhacking.kr/challenge/codeing/code3.html 이므로
=을 쓰고 뒤에 해당 문자열을 쭉 입력하면 된다.

http://webhacking.kr/challenge/codeing/code3.html?=youaregod~~~~~~~!
인데 그냥 해석된 "=youaregod~~~~~~~!"에서 replace 코드에 맞춰 '='을 삭제하고 Auth란에 입력하면 끝난다.
"""

import urllib2
import CookieConstants
import urllib

challengeUrl = "http://webhacking.kr/challenge/codeing/code3import CookieManagerquote("=youaregod~~~~~~~!")

httpRequest = urllib2.Request(challengeUrl + "?" + param)
CookieManager.addCookie("PHPSESSID=da0bd6cb852292c17cc2364c9dc6d334") # webhacking.kr에 로그인 하고 나온 cookie
httpRequest.add_header("Cookie", CookieManager.getCookie())

httpResponse = urllib2.urlopen(httpRequest).read()
print httpResponse
CookieManagerAlert으로 나오기 때문에 해당 접속 방법은 의미가 없다."
print "답은 [youaregod~~~~~~~!]"
