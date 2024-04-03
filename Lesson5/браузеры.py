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


# Chrome
# Задание 1. Клик по кнопке. 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(3)

for i in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

sleep(2)

delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

sleep(3)

print(len(delete_buttons))


# задание 2. Клик по кнопке без ID. 

options = webdriver.ChromeOptions() # у меня возникает ошибка, говорящая о блокировке сайта. Поэтому такая заплатка.
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)

#Откройте страницу http://uitestingplayground.com/dynamicid
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.maximize_window()

# Запуск скрипта 3 раза
for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ждем, пока кнопка синего цвета станет кликабельной
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))


sleep(2)

driver.quit()   

# задание 3. Клик по кнопке с CSS-классом. Я не совсем понимаю как 2 и 3 задание реализовать по-разному, поэтому просто продублировала код еще раз.

options = webdriver.ChromeOptions() # у меня возникает ошибка, говорящая о блокировке сайта. Поэтому такая заплатка.
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")

    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))


sleep(2)

driver.quit()   

# задание 4. Модальное окно
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)

try:
    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal"))) 
    
    close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p") 
    close_button.click()
    
finally:
    driver.quit()


# задание 5. Поле ввода

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")


sleep(3)

input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_element.send_keys("1000")

sleep(3)

input_element.clear()

sleep(3)

input_element.send_keys("999")

sleep(3)

driver.quit() 

# задание 6. Форма авторизации. Здесь у меня проблема: при загруженной библиотеке Key почему-то send_keys не определяются.

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

usernamefield = driver.find_elements(By.CSS_SELECTOR, "username")
passwordfield = driver.find_elements(By.CSS_SELECTOR, "password")


sleep(5)

usernamefield.send_keys("tomsmith") # здесь почему-то не подгружается библиотека с ключами.
passwordfield.send_keys("SuperSecretPassword!")

loginbutton = driver.find_elements(By.CSS_SELECTOR, "button")
loginbutton.click()


### Firefox
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

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    blue_button.click()

sleep(2)

driver.quit()

# задание 3. Клик по кнопке с CSS-классом. Я не совсем понимаю как 2 и 3 задание реализовать по-разному, поэтому просто продублировала код еще раз.

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()
driver.get("http://uitestingplayground.com/dynamicid")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    blue_button.click()

sleep(2)

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

usernamefield = driver.find_elements(By.CSS_SELECTOR, "username")
passwordfield = driver.find_elements(By.CSS_SELECTOR, "password")

sleep(2)

usernamefield.send_keys("tomsmith") # здесь почему-то не подгружается библиотека с ключами.
passwordfield.send_keys("SuperSecretPassword!")

loginbutton = driver.find_elements(By.CSS_SELECTOR, "button")
loginbutton.click()