from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
s=Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.taobao.com')
#标签定位
search_input=driver.find_element_by_id('q')
search_input.send_keys('Iphone')
#执行js代码
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
btn=driver.find_element_by_css_selector('.btn-search')
btn.click()
driver.get('https://www.baidu.com')
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(5)
driver.quit()



