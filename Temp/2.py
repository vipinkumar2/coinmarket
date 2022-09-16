from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(driver)

url = 'https://www.ems.com.cn/english/'

driver.get(url)

token = 'CY008445045CN'

token_space = driver.find_element(By.XPATH, value="//input[@class='el-input__inner']")

token_space.send_keys(token)
driver.find_element(By.XPATH, value="//i[@class='el-icon-search']").click()
time.sleep(8)

slider_container = driver.find_element(By.XPATH,value="//div[@class='slide-verify-slider']")
slider = driver.find_element(By.XPATH, value="//div[@class='slide-verify-slider-mask-item']")

# Perform sliding action
for x in range(10000):
    
    actions.move_to_element(slider).click_and_hold().move_by_offset(x*2, 0).release().perform()
    time.sleep(0.1)