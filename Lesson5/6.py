from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Открываем страницу
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
