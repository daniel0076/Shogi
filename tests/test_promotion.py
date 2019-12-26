from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class TestPromotion:

    def test_do_promote(self, selenium):
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
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[4]/td[6]//img")))
        # first hand move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[6]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[6]/td[7]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[5]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[5]/td[7]//img")))
        # second hand move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[3]/td[5]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[3]/td[5]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[5]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[4]/td[5]//img")))
        # first hand move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[5]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[5]/td[7]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[4]/td[7]//img")))
        # second hand move
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[3]/td[4]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[3]/td[4]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[4]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[4]/td[4]//img")))
        # move and promote
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[4]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[4]/td[7]//div[@class='piece selected']")))
        selenium.find_element_by_xpath("//table[@class='battlefield']/tbody/tr[3]/td[7]").click()
        wait.until(presence_of_element_located((By.XPATH, "//table[@class='battlefield']/tbody/tr[3]/td[7]//img")))
        wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '昇變' + "')]")))