from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

#Откройте страницу http://uitestingplayground.com/dynamicid
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
# Запуск скрипта 3 раза
for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ждем, пока кнопка синего цвета станет кликабельной
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "id='80d9ceae-a4cc-5d06-0e29-4630be816d36'")))


sleep(2)

driver.quit()        



