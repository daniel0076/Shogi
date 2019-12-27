from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pytest
import time
import os
import subprocess


@pytest.fixture(scope="session", autouse=True)
def prepare_account():
    print("Preparing for test")

    # clear database
    manage_path = os.path.join(os.path.dirname(__file__), '..', 'Shogi', 'manage.py')
    subprocess.run(["python3", manage_path, "flush", "--no-input"])

    selenium = webdriver.Chrome()
    # create accounts
    wait = WebDriverWait(selenium, 5)
    selenium.get("http://localhost:4200")
    selenium.find_element_by_xpath("/html/body/app-root/div/app-welcome/app-auth/nz-layout/nz-content/div/form/nz-form-item[3]/nz-form-control/div/span/a").click()
    selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input").send_keys("test")
    selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input").send_keys("test")
    selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[2]").click()
    wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '註冊成功' + "')]")))

    # create accounts 2
    selenium.get("http://localhost:4200")
    selenium.find_element_by_xpath("/html/body/app-root/div/app-welcome/app-auth/nz-layout/nz-content/div/form/nz-form-item[3]/nz-form-control/div/span/a").click()
    selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input").send_keys("test2")
    selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[2]/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input").send_keys("test")
    selenium.find_element_by_xpath("/html/body/div[1]/div[2]/div/nz-modal/div/div[2]/div/div/div[3]/button[2]").click()
    wait.until(presence_of_element_located((By.XPATH, "//*[contains(text(),'" + '註冊成功' + "')]")))

    time.sleep(1)

    selenium.find_element_by_name("username").send_keys("test")
    selenium.find_element_by_name("password").send_keys("test", Keys.ENTER)

    # create history
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

    # exit to create history
    selenium.find_element_by_xpath("//app-game//app-board/div[2]/button").click()
    selenium.find_element_by_xpath("//div[@class='ant-modal-confirm-btns']/button[2]").send_keys(Keys.ENTER)

    wait.until(presence_of_element_located((By.CLASS_NAME, "game-options")))

    selenium.close()