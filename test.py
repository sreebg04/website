from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
print("***************Loading Bing search***************")
browser.get('http://54.161.194.100:84/')
time.sleep(1)
print("***************Website Launched Successfully***************")
print(browser.title)
browser.quit()
