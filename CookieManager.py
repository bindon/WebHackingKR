import Cookie

cookie = Cookie.SimpleCookie()
    
def addCookie(key, value):
    cookie[key] = value

def getCookie():
    return ' '.join(['%s=%s;' % (currentCookie.key, currentCookie.value) for currentCookie in cookie.values()])
    
def clearCookie():
    cookie.clear()
    
def getOneCookie(key):
    return cookie.get(key).value if cookie.has_key(key) else ""