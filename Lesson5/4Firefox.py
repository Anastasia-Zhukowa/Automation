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
from webdriver_manager.firefox import GeckoDriverManager


import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)

try:
    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal"))) #modal - название появившегося модального окна
    
    # Нахождение кнопки Close и клик по ней
    close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p") # .modal-footer p - название кнопки закрыватия в модальном окне
    close_button.click()
    
finally:
    # Закрытие браузера
    driver.quit()
