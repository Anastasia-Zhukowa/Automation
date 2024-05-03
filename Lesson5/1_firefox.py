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

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(5)

# Пять раз кликните на кнопку "Add Element"
for i in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

sleep(2)

# Соберите со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

sleep(5)

# Выведите на экран размер списка
print(len(delete_buttons))

sleep(5)