import requests
import json
if __name__ == '__main__':
    #1指定url
    post_url='https://fanyi.baidu.com/sug'
    #2post请求参数处理
    word=input('enter a word:')
    data={
        'kw':word
    }
    #3ua
    headers={
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    #4请求发送
    response=requests.post(url=post_url,data=data,headers=headers)
    #5获取响应数据:json()返回的是obj 如果确认响应数据是jsonb类型才能使用json()
    dic_obj=response.json()
    #持久化存储
    fileName=word+'.json'
    fp=open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!!!')
