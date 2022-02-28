from selenium import webdriver
from lxml import etree
from selenium.webdriver.chrome.service import Service
from time import sleep
s=Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('http://scxk.nmpa.gov.cn:81/xk')
page_text=driver.page_source
tree=etree.HTML(page_text)
li_list=tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name=li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
driver.quit()
