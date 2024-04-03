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

# Находим поля для ввода имени пользователя и пароля
usernamefield = driver.find_elements(By.CSS_SELECTOR, "username")
passwordfield = driver.find_elements(By.CSS_SELECTOR, "password")

sleep(5)

# Вводим данные пользователя

usernamefield.send_keys("tomsmith") # здесь почему-то не подгружается библиотека с ключами.
passwordfield.send_keys("SuperSecretPassword!")


# Нажимаем кнопку Login
loginbutton = driver.find_elements(By.CSS_SELECTOR, "button")
loginbutton.click()