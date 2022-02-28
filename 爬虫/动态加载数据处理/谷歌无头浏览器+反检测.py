from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from time import sleep
#无可视化界面
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#实现规避检测
option=ChromeOptions()
option.add_experimental_option('excludeSwitcher',['enable-automation'])

s=Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=s,chrome_options=chrome_options,options=option)
driver.get('https://www.baidu.com')
print(driver.page_source)
sleep(2)
driver.quit()