import requests
from lxml import etree
import os
if __name__ == '__main__':
    url='https://pic.netbian.com/4kmeinv/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)
    #response.encoding='utf-8'
    page_text=response.text
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//div[@class="slist"]/ul/li')
    #创建文件夹
    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')
    for li in li_list:
        img_src='https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        #print(img_name,img_src)
        img_data=requests.get(url=img_src,headers=headers).content
        img_path='piclibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功')
