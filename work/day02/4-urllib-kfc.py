import urllib.request

import urllib.parse

# ajax post
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid&cname=&pid=31&pageIndex=8&pageSize=10'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}
'''
cname: 上海
pid: 
pageIndex: 2
pageSize: 10
'''
if __name__ == '__main__':
    city = input('请输入查询城市:')
    page = int(input('请输入查询页码'))
    for p in range(1,page+1):
        form = {
        'cname':city,
        'pid':p,
        'pageindex':p,
        'pageSize': 10
}
        form = urllib.parse.urlencode(form).encode('utf8')
        request = urllib.request.Request(url=url,headers=headers,data=form)

        response = urllib.request.urlopen(request)

        content = response.read().decode('utf8')

        with open('./download/%s肯德基第%d页.json'%(city,p),'wb') as fp:
            fp.write(content.encode('utf-8'))







