from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class TestHistory:

    def test_history(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[4]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[1]/div/div")))
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/ul/li").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-game/nz-layout/nz-content/p[1]")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-game/nz-layout/nz-content/div[2]/button[2]").click()
        selenium.find_element_by_xpath("/html/body/app-root/div/app-game/nz-layout/nz-content/div[2]/button[2]").click()
        # exit
        selenium.find_element_by_xpath("//app-game//app-board/div[2]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '是否確認結束' + "')]")))
        selenium.find_element_by_xpath("//div[@class='ant-modal-confirm-btns']/button[2]").send_keys(Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))

    def test_history_empty(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test2")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[4]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[1]/div/div")))
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[1]").click()
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))


