import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    #获取页面源码数据
    url='https://bj.58.com/ershoufang/'
    page_text=requests.get(url=url,headers=headers).text
    #数据解析
    tree=etree.HTML(page_text)
    #存储标签
    div_list=tree.xpath('//section[@class="list"]/div')
    fp=open('58.txt','w',encoding='utf-8')
    for li in div_list:
        title=li.xpath('./a/div(property-content-title)/h3/')[0]
        print(title)
        fp.write(title+'\n')


