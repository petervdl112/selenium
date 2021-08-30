from selenium import webdriver
from selenium.webdriver.common.keys import Keys #om enter etc. door te kunnen geven
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


#PATH = 'C:/Program Files (x86)/chromedriver.exe' #voor windows
#driver = webdriver.Chrome(PATH) #voor windows

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(5) #zelfde als WebDriverWait in principe, alleen iets makkelijker.

cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1, -1)]

#als je actions.perform() doet dan worden alle acties onder actions variable uitgevoerd. 
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()

    count = int(cookie_count.text.split(" ")[0])
    print(count)

    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
