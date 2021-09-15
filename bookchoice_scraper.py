from  selenium import webdriver
from selenium.webdriver.common.keys import Keys #acces to enter, esc etc..
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:\Book_downloads'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(PATH, options=chrome_options)


driver.get("https://www.bookchoice.com/")


driver.implicitly_wait(2)
driver.maximize_window()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//button[normalize-space()="Accepteer cookies"]').click()

time.sleep(1)

boeken = driver.find_element_by_xpath('//a[contains(text(), "Boeken")]')
driver.implicitly_wait(2)
boeken.click()

inloggen = driver.find_element_by_link_text('Inloggen')
inloggen.click()
driver.implicitly_wait(3)

email = driver.find_element_by_id('login-email')
driver.implicitly_wait(1)
email.send_keys('p_vdlinde@hotmail.com')
driver.implicitly_wait(1)
password = driver.find_element_by_id('login-password')
password.send_keys('pipo1980_')
driver.implicitly_wait(1)
inloggen2 = driver.find_element_by_xpath('//button[normalize-space()="Inloggen"]')
inloggen2.click()


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
#print(list)
f = open('books.html', 'w')

for ref in list:
    driver.get(ref)
    time.sleep(2)
    samenvatting = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/section/div/div[2]/div[1]/div/div[2]/div[2]/p')
    print(samenvatting.text)
    f.write(samenvatting.text)
    download = driver.find_element_by_xpath('//span[normalize-space()="Download e-book"]').click()
    time.sleep(20)