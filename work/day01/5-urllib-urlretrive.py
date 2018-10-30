import urllib.request
import requests
url="http://www.shubao21.com/user/login"
html=requests.get()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'

}

code=input("")
data = {
    'username': '1600826716',
    'password': 'password',
    'code': code,
}


url ='http://www.czttxt.com/modules/article/txtarticle.php?id=85902'
urllib.request.urlretrieve(url=url,filename='./note.txt')

# /book/down/189552/1


# href="/modules/article/txtarticle.php?id=75109"
