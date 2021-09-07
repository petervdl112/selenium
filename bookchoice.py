from  selenium import webdriver
from selenium.webdriver.common.keys import Keys #acces to enter, esc etc..
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://www.bookchoice.com/")


driver.implicitly_wait(2)
driver.find_element_by_xpath('//button[normalize-space()="Accepteer cookies"]').click()

driver.implicitly_wait(10)

inloggen = driver.find_element_by_link_text('Inloggen')
inloggen.click()
driver.implicitly_wait(3)

email = driver.find_element_by_id('login-email')
driver.implicitly_wait(2)
email.send_keys('p_vdlinde@hotmail.com')
driver.implicitly_wait(1)
password = driver.find_element_by_id('login-password')
password.send_keys('pipo1980_')




time.sleep(60)

#nu wel iets toch?