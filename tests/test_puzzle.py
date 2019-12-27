from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class TestPuzzle:

    def test_puzzle(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[3]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/nz-modal/div/div[2]/div/div/div[1]/div/div")))
        selenium.find_element_by_xpath("/html/body/div[1]/div[3]/div/nz-modal/div/div[2]/div/div/div[2]/ul/li").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-game/nz-layout/nz-content/div[1]/app-board/div[1]/div/div[2]/div[2]/table/tr[2]/td[3]/app-piece/div/img")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-game/nz-layout/nz-content/div[1]/app-board/div[1]/div/div[2]/div[2]/table/tr[2]/td[3]/app-piece/div/img").click()
        selenium.find_element_by_xpath("/html/body/app-root/div/app-game/nz-layout/nz-content/div[1]/app-board/div[1]/div/div[1]/table/tbody/tr[2]/td[2]").click()
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '棋局結束' + "')]")))

    def test_puzzle_empty(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test2")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[4]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[1]/div/div")))
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[1]").click()
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))


