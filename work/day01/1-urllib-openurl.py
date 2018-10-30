import urllib

# response = requests.get('https://www.toutiao.com/')
import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url=url)

content = response.read().decode('utf-8')
print(content)

# print(response.text)
# print(response.content.decode())
