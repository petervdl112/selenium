from  selenium import webdriver
from selenium.webdriver.common.keys import Keys #acces to enter, esc etc..
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://www.bookchoice.com/")


time.sleep(20)

driver.implicitly_wait(2)
driver.find_element_by_xpath('//button[normalize-space()="Accepteer cookies"]').click()

inloggen = driver.find_element_by_id('login-link')
driver.implicitly_wait(3)
email = driver.find_element_by_id('login-email')


time.sleep(60)