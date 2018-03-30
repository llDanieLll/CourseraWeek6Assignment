import urllib.request

try:
    url = 'http://www.google.com/search?q=Daniel'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0'
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close
except Exception as e:
    print (str(e))
