#UA检测:门户网站的服务器会检测对应载体的身份标识，如果检测到请求的载体是浏览器说明是正常请求
#UA:User-Agent
#UA伪装:让爬虫对应的请求载体身份标识伪装成一款浏览器
import requests
if __name__ == '__main__':
    url='https://www.sogou.com/web'
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    #处理url携带的参数：封装到字典中
    kw=input('enter a word')
    param={
        'query':kw
    }
    #对指定的url发起的请求的url是携带参数的,并且请求过程中处理了参数
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功')
