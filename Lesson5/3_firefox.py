from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()


#Откройте страницу 
driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

sleep(2)

ok_button = driver.find_element(By.ID, "modalOkButton")
ok_button.click()

sleep(2)

for _ in range(3):
    blue_button.click()
    sleep(2)
    ok_button.click()
    sleep(2)

driver.quit()