from  selenium import webdriver
from selenium.webdriver.common.keys import Keys #acces to enter, esc etc..
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://www.bookchoice.com/")

driver.implicitly_wait(2)
driver.find_element_by_xpath('//button[normalize-space()="Accepteer cookies"]').click()


time.sleep(60)