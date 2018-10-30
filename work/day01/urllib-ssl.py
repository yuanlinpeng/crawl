import urllib.request
import ssl


# 设置进行网络请求，忽略，ssl验证
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb/'

# request = urllib.request.Request(url=url)

response = urllib.request.urlopen(url=url)
print(response.read().decode('utf8'))

