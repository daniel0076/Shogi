from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

class TestUserSettings:

    def test_edit_settings(self, selenium):
        wait = WebDriverWait(selenium, 5)

        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("//app-setting/div/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//div[@class='ant-modal-content']")))
        # click on settings
        old_value = selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").text
        selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").send_keys(Keys.ENTER)
        selenium.find_element_by_xpath("//div[contains(@class, 'ant-modal-footer')]/button[2]").click()
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '正在儲存' + "')]")))

        # check that settings changed
        selenium.find_element_by_xpath("//app-setting/div/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//span[text()='Show Territory']")))
        new_value = selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").text

        if old_value == "On":
            assert new_value == "Off"
        elif old_value == "Off":
            assert new_value == "On"
