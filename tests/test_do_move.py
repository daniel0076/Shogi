from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class TestDoMove:

    def test_move_pieces(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("//app-select/nz-layout/nz-content/div/div[1]/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr")))
        # first hand move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[7]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[7]/td[7]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[6]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[6]/td[7]//img")))
        # second hand move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[3]/td[6]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[3]/td[6]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[6]").click()
        cell = wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[4]/td[6]//img")))

        # If the test finally goes here, the test is passed
        # Otherwise, TimeoutException will be raised by wait.until
        assert True

    def test_invalid_click(self, selenium):
        wait = WebDriverWait(selenium, 5)
        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("//app-select/nz-layout/nz-content/div/div[1]/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr")))
        # click on blank
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[5]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '你不能動這顆棋!' + "')]")))
        # click on opponent chess
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[3]/td[1]").click()
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '你不能動這顆棋!' + "')]")))

        # If the test finally goes here, the test is passed
        assert True

    def test_invalid_move(self, selenium):
        wait = WebDriverWait(selenium, 5)
        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("//app-select/nz-layout/nz-content/div/div[1]/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr")))
        # click valid chess but invalid move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[7]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[7]/td[7]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[8]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '無法走到那' + "')]")))