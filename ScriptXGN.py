from selenium import webdriver
from selenium.webdriver.common.keys import Keys #om enter etc. door te kunnen geven
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#1e video on selenium TechWithTim

PATH = 'C:/Program Files (x86)/chromedriver.exe' #voor windows
driver = webdriver.Chrome(PATH) #voor windows

#driver = webdriver.Chrome()

driver.get('https://www.xgn.nl/artikel/xbox-series-x-series-s-kopen-pre-order')

#grab search results. Textbox "search" has HTML "value_name='s'"


driver.implicitly_wait(2)
driver.find_element_by_xpath('//button[normalize-space()="IK GA AKKOORD"]').click()

time.sleep(2)

test_naam = driver.find_element_by_tag_name("article").text

if "Update 26" in test_naam:
    print('yes')
else:
    print('no')






