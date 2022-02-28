# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text=requests.get(url=url,headers=headers).content.decode('utf-8')
    soup=BeautifulSoup(page_text,'lxml')
    li_list=soup.select('.book-mulu > ul > li')
    fp=open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.a.string
        detail_url='https://www.shicimingju.com/'+li.a['href']
        detail_page_text=requests.get(url=detail_url,headers=headers).content.decode('utf-8')
        detail_soup=BeautifulSoup(detail_page_text,'lxml')
        div_tag=detail_soup.find('div',class_='chapter_content')
        content=div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功')



