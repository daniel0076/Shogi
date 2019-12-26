from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class TestGameTypeSelection:

    def test_local(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[1]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-game/nz-layout/nz-content/p[1]")))

    def test_online(self, selenium):
        driver1 = webdriver.Chrome()
        wait1 = WebDriverWait(driver1, 5)
        driver1.get("http://localhost:4200")
        driver1.find_element_by_name("username").send_keys("test")
        driver1.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait1.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        driver1.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[2]/button").click()
        wait1.until(presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-game/nz-layout/nz-content/p[1]")))
        driver2 = webdriver.Chrome()
        wait2 = WebDriverWait(driver2, 5)
        driver2.get("http://localhost:4200")
        driver2.find_element_by_name("username").send_keys("test2")
        driver2.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait2.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        driver2.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[2]/button").click()
        wait2.until(presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-game/nz-layout/nz-content/p[2]")))
        driver1.close()
        driver2.close()

    def test_history(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[4]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[1]/div/div")))

    def test_history_exit(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[4]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[1]/div/div")))
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[1]").click()
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))

    def test_puzzle(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("/html/body/app-root/div/app-select/nz-layout/nz-content/div/div[3]/button").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/nz-modal/div/div[2]/div/div/div[1]/div/div")))
