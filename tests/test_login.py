from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class TestLogin:

    def test_login_suc(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))

    def test_login_wrong_password(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        sleep(4)
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("testt", Keys.ENTER)
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span")))
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '帳號密碼錯誤，或使用者不存在或已登入系統' + "')]")))

    def test_login_invalid_username(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        sleep(4)
        selenium.find_element_by_name("username").send_keys("testt")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span")))
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '帳號密碼錯誤，或使用者不存在或已登入系統' + "')]")))
