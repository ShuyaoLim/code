from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from time import sleep
s=Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame('iframeResult')
div=driver.find_element_by_id('draggable')
#动作链
action=ActionChains(driver)
#点击长按指定的标签
action.click_and_hold(div)
for i in range(5):
    #perform立即执行动作链操作
    action.move_by_offset(17,0).perform()
    sleep(0.3)
#释放动作链
action.release()
driver.quit()
