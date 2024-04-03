from selenium import webdriver
from time import sleep
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



# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Запускаем цикл 3 раза
for _ in range(3):
    driver.get("http://uitestingplayground.com/classattr")

    # Ждем, пока кнопка синего цвета станет кликабельной
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "btn-primary")))
    sleep(2)
    # Находим и нажимаем на синюю кнопку
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()

    sleep(2)
    # Переключаемся на алерт и нажимаем на кнопку "OK"
    ok_button = driver.find_element(By.ID, "modalOkButton")
    ok_button.click()
    
    time.sleep(2)  # Делаем паузу для наглядности

# Закрываем драйвер
driver.quit()