from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открываем сайт
driver.get("http://uitestingplayground.com/classattr")


# Нажимаем на синюю кнопку
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

# Ждем 2 секунды
time.sleep(2)

# Нажимаем на кнопку "OK" в появившемся окне
ok_button = driver.find_element(By.ID, "modalOkButton")
ok_button.click()

# Ждем 2 секунды
time.sleep(2)

# Повторяем цикл 3 раза
for _ in range(3):
    blue_button.click()
    time.sleep(2)
    ok_button.click()
    time.sleep(2)

# Закрываем браузер
driver.quit()
