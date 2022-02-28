import requests
url='https://www.baidu.com/s?wd=ip'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
page_text=requests.get(url=url,headers=headers,proxies={"http":"14.215.212.37:9168"}).text
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)