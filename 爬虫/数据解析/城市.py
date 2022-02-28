import requests
from lxml import etree
if __name__ == '__main__':
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    # }
    # url='https://www.aqistudy.cn/historydata/'
    # page_text=requests.get(url=url,headers=headers).text
    # tree=etree.HTML(page_text)
    # hot_li_list=tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names=[]
    # for li in hot_li_list:
    #     hot_city_name=li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    # #解析全部城市名称
    # city_names_list=tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name=li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    # print(all_city_names,len(all_city_names))


    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    url='https://www.aqistudy.cn/historydata/'
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    a_list=tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names=[]
    for a in a_list:
        city_name=a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))