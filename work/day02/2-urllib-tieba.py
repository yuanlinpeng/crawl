import urllib.request

import urllib.parse

url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'

}


def write_to_file(content, i):
    with open('./download/贴吧第%d页.html'%(i+1),'wb') as fp:
        fp.write(content.encode('utf8'))
        print('贴吧第%d保存成功'%(i+1))


def load_url_data(key,i):
    for i in range(num):
        url_detail = url%(key,i*50)
        request = urllib.request.Request(url=url_detail,headers=headers)

        response = urllib.request.urlopen(request)

        content = response.read().decode('utf8')

        write_to_file(content,i)


if __name__ == '__main__':
    key = input('请输入贴吧关键字')

    key = urllib.parse.quote(key)
    try:
        num = int(input('请输入爬取多少页'))
    except Exception as e:
        print('请输入数字型数据:')
        num = int(input('请输入爬取多少页'))

    load_url_data(key,num)