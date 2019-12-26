from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class TestLocal:

    def test_local(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[1]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-game/nz-layout/nz-content/p[1]")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-game/nz-layout/nz-content/div[1]/app-board/div[2]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-game/nz-layout/nz-content/p[1]")))
        
