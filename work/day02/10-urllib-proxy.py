import urllib.request

proxies = {'https':'27.22.104.28:39560'}

proxyHandler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxyHandler)

response = opener.open(fullurl='http://www.baidu.com')

content = response.read().decode('utf8')

with open('./baidu.html','w',encoding='utf8') as fp:
    fp.write(content)