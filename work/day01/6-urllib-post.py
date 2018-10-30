import urllib.parse
import urllib.request
url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
# url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'
# url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action='
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
#
# }

form = {
'start': 0,'limit': 1
}
data = urllib.parse.urlencode(form).encode('utf8')

response = urllib.request.urlopen(url=url,data=data)

print(response.read().decode('utf8'))
# request = urllib.request.Request(url=url,headers=headers)

# response =urllib.request.urlopen(request)

# print(response.read().decode('utf8'))
# urllib.request.urlretrieve(url=url,filename='./movie.json')



