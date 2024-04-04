from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


for i in range(3):
    # Создаем экземпляр драйвера браузера
    driver = webdriver.Chrome()

# Открываем сайт
    driver.get("http://uitestingplayground.com/classattr")
    sleep(2)

# Нажимаем на синюю кнопку
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()

# Ждем 2 секунды
    sleep(2)

# Закрываем браузер
    driver.quit()


