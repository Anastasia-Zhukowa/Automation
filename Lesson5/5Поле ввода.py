from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# Откройте страницу http://the-internet.herokuapp.com/inputs.
#driver = webdriver.Firefox()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")


sleep(5)

# Введите в поле текст 1000.
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_element.send_keys("1000")

sleep(5)


# Очистите это поле (метод clear).
input_element.clear()

sleep(5)

# Введите в это же поле текст 999.
input_element.send_keys("999")

sleep(5)

# Закройте браузер.
driver.quit()