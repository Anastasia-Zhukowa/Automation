from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу для входа
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

