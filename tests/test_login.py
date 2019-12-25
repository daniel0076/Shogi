from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome() as driver:
    driver.get("http://localhost:4200")
    driver.find_element_by_name("username").send_keys("test")
    driver.find_element_by_name("password").send_keys("test", Keys.ENTER)

    wait = WebDriverWait(driver, 5)
    result = wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
    #print(first_result.get_attribute("textContent"))