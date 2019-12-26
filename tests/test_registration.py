from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

class TestRegistration:

    def test_registration_suc(self, selenium):
        wait = WebDriverWait(selenium, 5)
        selenium.get("http://localhost:4200")
        sleep(3)
        selenium.find_element_by_xpath("/html/body/app-root/div/app-welcome/app-auth/nz-layout/nz-content/div/form/nz-form-item[3]/nz-form-control/div/span/a").click()
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input").send_keys("ryan")
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input").send_keys("test")
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[2]").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span")))
        text = selenium.find_element_by_xpath("/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span").text
        assert text == "註冊成功"

    def test_registration_invalid_account(self, selenium):
        wait = WebDriverWait(selenium, 5)
        selenium.get("http://localhost:4200")
        sleep(3)
        selenium.find_element_by_xpath("/html/body/app-root/div/app-welcome/app-auth/nz-layout/nz-content/div/form/nz-form-item[3]/nz-form-control/div/span/a").click()
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input").send_keys("test")
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input").send_keys("test")
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[2]").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span")))
        text = selenium.find_element_by_xpath("/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span").text
        assert text == "Username already be used"

    def test_registration_invalid_password(self, selenium):
        wait = WebDriverWait(selenium, 5)
        selenium.get("http://localhost:4200")
        sleep(3)
        selenium.find_element_by_xpath("/html/body/app-root/div/app-welcome/app-auth/nz-layout/nz-content/div/form/nz-form-item[3]/nz-form-control/div/span/a").click()
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input").send_keys("ryan123")
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input").send_keys("zz")
        selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[2]").click()
        wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span")))
        text = selenium.find_element_by_xpath("/html/body/div[1]/div[1]/div/nz-message-container/div/nz-message/div/div/div/span").text
        assert text == "Short password"
