import os
import urllib.request

# 将用户名和密码保存到环境变量中

pw = os.environ.get('')

proxyServer = os.environ.get('proxyServer')

user = os.environ.get('proxyuser')

proxies = {'http':'%s:%s@%s'%(user,pw,proxyServer)}

proxy_handler = urllib.request.ProxyHandler(proxies=proxies)


opener = urllib.request.build_opener(proxy_handler)

response = opener.open('http://www.baidu.com/')

print(response.read().decode('utf-8'))