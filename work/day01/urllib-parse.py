import urllib.parse
import urllib.request

url = 'https://www.baidu.com/s?wd=%s'
# key = input('请输入查询的关键字')
# key = urllib.parse.quote(key)
# key = urllib.parse.urlencode({'wd':'s8赛程'.encode()})
# url1 = url + key
# print(url1)
key = input('请输入查询的关键字')

key = urllib.parse.quote(key)

url = url%(key)

print(url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())
