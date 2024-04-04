from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


import os
from selenium import webdriver

# Задание 1.

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(5)

for i in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

sleep(2)

delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

sleep(5)

print(len(delete_buttons))


# задание 2. Клик по кнопке без ID. 
geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

driver.get("http://uitestingplayground.com/dynamicid")

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Firefox(options=options)

for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    blue_button.click()

sleep(2)

driver.quit()

# задание 3. Клик по кнопке с CSS-классом.


for i in range(3):
    driver = webdriver.Firefox()

    driver.get("http://uitestingplayground.com/classattr")
    sleep(2)

    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()

    sleep(2)

    # ok_button = driver.find_element(By.ID, "modalOkButton")
    #ok_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    #ok_button.click()

    driver.quit()



# задание 4. Модальное окно

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)

try:
    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal"))) #modal - название появившегося модального окна
    
    close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p") # .modal-footer p - название кнопки закрыватия в модальном окне
    close_button.click()
    
finally:
    driver.quit()

#  задание 5. Поле ввода
geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(5)

input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_element.send_keys("1000")

sleep(3)

input_element.clear()

sleep(3)

input_element.send_keys("999")

sleep(2)

driver.quit()


# задание 6. Форма авторизации. Здесь у меня проблема: при загруженной библиотеке Key почему-то send_keys не определяются.

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

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

