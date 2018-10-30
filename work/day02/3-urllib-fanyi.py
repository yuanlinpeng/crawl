import urllib.parse

import urllib.request

import json

# post请求,百度翻译对form要求很严格
url = 'https://fanyi.baidu.com/v2transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Host': 'fanyi.baidu.com',

    'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=%E4%B8%AD%E5%9B%BD&keyfrom=baidu&smartresult=dict&lang=auto2zh',

    'Cookie': 'BIDUPSID=78F481ABB0748250D9BAC266BC0137A5; PSTM=1534819948; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=71004D080AB7279F7CA1F0256D092FE1:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=nd0U0JJR3RLSnMwaDdBSWt-NGJyZWNlaXdxcVpwc2l6SHV1emM5RDBoY2t1TTFiQVFBQUFBJCQAAAAAAAAAAAEAAAChhDKUxL5s1MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACQrplskK6ZbU; __cfduid=d04f31f793bb449f8bc485a7d881740521539153894; MCITY=-289%3A; locale=zh; H_PS_PSSID=1464_21093_22160; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1540816629,1540816757,1540817037,1540818177; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1540818276; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',

}


'''
from=zh&
to=en&
query=%E4%B8%AD%E5%9B%BD&
simple_means_flag=3&
sign=777849.998728&
token=093b95987b40c10ae8d47475b8d32ea5'''

key = input('请输入翻译的汉字')
form = {
    'from': 'zh',
    'to': 'en',
    'query': key,
    'simple_means_flag': '3',
    'sign': '777849.998728',
    'token':'093b95987b40c10ae8d47475b8d32ea5'

}
form = urllib.parse.urlencode(form).encode('utf-8')

request = urllib.request.Request(url=url,headers=headers,data=form)

# response = urllib.request.urlopen(url=url,data=form)

response = urllib.request.urlopen(request)

content = response.read().decode('utf8')
# print(content)

# 首先使用json加载,编码utf8
# 然后dump 编码不采用ascii码
content = json.dumps(json.loads(content,encoding='uft8'),ensure_ascii=False)
print(content)
# print(response.read().decode('utf8'))
