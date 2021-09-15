from  selenium import webdriver
from selenium.webdriver.common.keys import Keys #acces to enter, esc etc..
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.bookchoice.com/")


driver.implicitly_wait(2)
driver.maximize_window()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//button[normalize-space()="Accepteer cookies"]').click()

time.sleep(1)

boeken = driver.find_element_by_xpath('//a[contains(text(), "Boeken")]')
driver.implicitly_wait(2)
boeken.click()

time.sleep(1)
#test = driver.find_elements_by_xpath('//img[@class="w-100 h-100"]')
#for element in test:
#    print(element.get_attribute("src"))


test2 = driver.find_elements_by_xpath('//div[@book="[object Object]"]/a')
list = []
for element in test2:
    list.append(element.get_attribute('href'))
    #element_str = element.get_attribute('href')

    #(element.get_attribute('href'))
    time.sleep(2)
    #driver.get(element_str)
print(list)
for ref in list:
    driver.get(ref)
    time.sleep(10)