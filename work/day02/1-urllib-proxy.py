import re

import urllib.request
# <td>([\d\.a-zA-Z\/]+)</td>
partten = r'<td>([\d\.a-zA-Z\/]+)+</td>'

with open('proxy.html','r',encoding='utf8') as fp:
    proxy = fp.read()
    p = re.compile(pattern=partten)
    proxies = re.findall(pattern=p, string=proxy)
    print(proxies)