from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

class TestTerritory:

    def test_show_territory(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))

        # check territory is on
        selenium.find_element_by_xpath("//app-setting/div/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//div[@class='ant-modal-content']")))
        # click on settings
        current_value = selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").text

        if current_value == "Off": # turn if on
            # click on settings
            selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").send_keys(Keys.ENTER)
            selenium.find_element_by_xpath("//div[contains(@class, 'ant-modal-footer')]/button[2]").click()
            wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '正在儲存' + "')]")))
            time.sleep(2)

        selenium.find_element_by_xpath("//app-select/nz-layout/nz-content/div/div[1]/button").send_keys(Keys.ENTER)
        # wait for angular game
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr")))
        # check territory color
        white_side = selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[1]")
        assert white_side.get_attribute("ng-reflect-ng-class") == "white-side"
        neutral_side = selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[5]/td[1]")
        assert neutral_side.get_attribute("ng-reflect-ng-class") == "neutral-side"
        black_side = selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[6]/td[1]")
        assert black_side.get_attribute("ng-reflect-ng-class") == "black-side"

        # check territory color after move
        # do move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[7]/td[1]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[7]/td[1]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[6]/td[1]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[6]/td[1]//img")))
        # check territory color
        white_side = selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[1]")
        assert white_side.get_attribute("ng-reflect-ng-class") == "white-side"
        middle = selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[5]/td[1]")
        assert middle.get_attribute("ng-reflect-ng-class") == "black-side"
        black_side = selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[6]/td[1]")
        assert black_side.get_attribute("ng-reflect-ng-class") == "black-side"

    def test_turn_off_territory(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("//app-setting/div/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//div[@class='ant-modal-content']")))
        # click on settings
        current_value = selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").text

        if current_value == "On": # turn if off
            # click on settings
            selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").send_keys(Keys.ENTER)
            selenium.find_element_by_xpath("//div[contains(@class, 'ant-modal-footer')]/button[2]").click()
            wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '正在儲存' + "')]")))
            time.sleep(1)

        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("//app-select/nz-layout/nz-content/div/div[1]/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr")))
        # check territory color
        white_side = selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[1]")
        assert white_side.get_attribute("ng-reflect-ng-class") == "default"