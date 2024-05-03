from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Запуск браузера
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
driver.find_element(By.ID, "ajaxButton").click()

# Ожидание появления зеленой плашки
wait = WebDriverWait(driver, 10)
green_box = wait.until(EC.visibility_of_element_located((By.ID, "ajaxDiv")))

# Получение текста из зеленой плашки
text = green_box.text

# Вывод текста в консоль
print(text)

# Закрытие браузера
driver.quit()