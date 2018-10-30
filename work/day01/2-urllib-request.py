import urllib
import urllib.request

# 构造联网请求

url = 'https://www.baidu.com/'

# 构造请求头,爬虫时的第一层伪装
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'

}

request = urllib.request.Request(url=url, headers=headers)

# request.add_header('Host','www.baidu.com')
#
response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))


# response = urllib.request.urlopen(request)

# print(response.read().decode('utf'))