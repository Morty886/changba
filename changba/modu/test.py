import re
import requests
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup

def new_url(url):
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    cc = soup.find_all('div', class_='title')[0]
        #print('歌曲:', str(cc)[19:-6])  # 下载歌曲的名字
    music_name = str(cc)[19:-6]
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", r.text)
    cc = ''
    for i in urls:
        parseResult = parse.urlparse(i)
        if parseResult.netloc == 'lzscuw.changba.com':
            cc = i
        elif parseResult.netloc == 'qiniuuwmp3.changba.com':
            cc = i

    return cc



a = new_url('http://changba.com/s/Hlqfw1lhOfc_4XNW5MSX1w')
print(a)