from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

class TestStoreSettings:

    def test_store_settings(self, selenium):
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
        time.sleep(1)
        selenium.find_element_by_xpath("//div[contains(@class, 'ant-modal-footer')]/button[2]").click()
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '正在儲存' + "')]")))
        time.sleep(2)

        # check that settings changed
        selenium.find_element_by_xpath("//app-setting/div/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//span[text()='Show Territory']")))

        if old_value == "On":
            wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + 'Off' + "')]")))
            new_value = "Off"
        elif old_value == "Off":
            wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + 'On' + "')]")))
            new_value = "On"

        time.sleep(2)

        # reconnect
        selenium.get("http://localhost:4200")
        selenium.find_element_by_name("username").send_keys("test")
        selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)
        wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))
        selenium.find_element_by_xpath("//app-setting/div/button").click()
        # wait for angular render
        wait.until(presence_of_element_located((By.XPATH, "//div[@class='ant-modal-content']")))
        # check the value
        value_after_reconnect = selenium.find_element_by_xpath("//span[text()='Show Territory']/following-sibling::button").text
        assert value_after_reconnect == new_value