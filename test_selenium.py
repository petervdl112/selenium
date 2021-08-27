

from  selenium import webdriver
from selenium.webdriver.common.keys import Keys #acces to enter, esc etc..
import time

#order: Id, name, class name (not unique!)
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
search = driver.find_element_by_name("s")

search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)


