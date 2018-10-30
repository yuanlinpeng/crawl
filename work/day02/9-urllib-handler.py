import urllib.request

http_handler = urllib.request.HTTPHandler()


# 方式一，直接使用opener发送请求
opener = urllib.request.build_opener(http_handler)
# response = opener.open()
# 方式二,将opener作为参数设置给urllib.request.urlopen
# opener 去全局的联网请求
urllib.request.install_opener(opener)

response = urllib.request.urlopen('http://www.baidu.com')

print(response.read().decode('utf-8'))