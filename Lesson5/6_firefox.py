from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait # этот модуль используется, чтобы дождаться загрузки окна 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/login")

sleep(2)

username = '#username'
username_input = driver.find_element(By.CSS_SELECTOR, username)
username_input.send_keys("tomsmith")
sleep(1)

password = '#password'
password_input = driver.find_element(By.CSS_SELECTOR, password)
password_input.send_keys("SuperSecretPassword!")

sleep(2)


# Нажимаем кнопку "Login"
login_button = "button[type='submit']"
login_button = driver.find_element(By.CSS_SELECTOR, login_button)
login_button.click()

sleep(2)

# Закрываем браузер
driver.quit()

