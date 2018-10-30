import urllib

import urllib.request

url = 'https://www.douban.com/people/184879949/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Cookie': 'bid=HfWD5gbtbuM; gr_user_id=1331fed8-2adf-483b-9d87-020b0b225e2c; _vwo_uuid_v2=D995703CB3B9F73317EE3AEA53E7C4DAC|c316963da7d63e650642fb84fb63f130; ll="108296"; douban-fav-remind=1; __utmv=30149280.18487; __yadk_uid=PA1iz0DcRAUyjklFDc12kXGtxhed2OJu; viewed="30271484_1944726"; ps=y; dbcl2="184879949:GT6AW0fYMy8"; push_noty_num=0; push_doumail_num=0; ck=snao; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1540826997%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dc1YwEOscX9lvNEYYfR-ALzwY8h-iSN5w3Gdr1N8TfYSgMnUst_CgpO1OlRAvZJ2q%26wd%3D%26eqid%3De30e46f40003da37000000025bd7276f%22%5D; _pk_ses.100001.8cb4=*; ap_v=0,6.0; __utma=30149280.1872490020.1534991495.1540782532.1540827000.22; __utmc=30149280; __utmz=30149280.1540827000.22.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; douban-profile-remind=1; _pk_id.100001.8cb4=123298ee3cec5c11.1536161294.12.1540827040.1540534462.; __utmb=30149280.8.10.1540827000'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))
