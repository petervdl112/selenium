from selenium import webdriver
from selenium.webdriver.common.keys import Keys #om enter etc. door te kunnen geven
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#2e video on selenium TechWithTim
PATH = '/Users/PvdL/Documents/Programming/Selenium_test/chromedriver'
driver = webdriver.Chrome()

driver.get('https://techwithtim.net')

link = driver.find_element_by_link_text('Python Programming')
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )

    element.click()

    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )

    element2.click()
    time.sleep(5)

    driver.back()
    driver.back()
    driver.back()

finally:
    pass
