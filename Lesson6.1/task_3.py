from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# создаем новый экземпляр двайвера
driver = webdriver.Chrome()

# прописываем драйвер ожидания
driver.implicitly_wait(10)

# запускаем сайт и кликаем на кнопку
driver.get("https://www.saucedemo.com/")

sleep(2)

# Находим поле ввода и вводим текст
username = '#user-name'
username_input = driver.find_element(By.CSS_SELECTOR, username)
username_input.send_keys("standard_user")

password = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password)
password_input.send_keys("secret_sauce")

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

sleep(2)

add_backpack = "#add-to-cart-sauce-labs-backpack"
add_backpack = driver.find_element(By.CSS_SELECTOR, add_backpack).click()

add_tshirt = "#add-to-cart-sauce-labs-bolt-t-shirt"
add_tshirt = driver.find_element(By.CSS_SELECTOR, add_tshirt).click()

add_onesie = "#add-to-cart-sauce-labs-onesie"
add_onesie = driver.find_element(By.CSS_SELECTOR, add_onesie).click()

cart_button = "#shopping_cart_container"
cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "shopping_cart_container")))
cart_button.click()

sleep(2)

#checkout = '#checkout'
checkout =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'checkout')))
checkout.click()

sleep(2)

first_name = '#first-name'
first_name_input = driver.find_element(By.CSS_SELECTOR, first_name)
first_name_input.send_keys("Anastasia")

last_name = '#last-name'
last_name_input = driver.find_element(By.CSS_SELECTOR, last_name)
last_name_input.send_keys("Zhukova")

code = "#postal-code"
code_input  = driver.find_element(By.CSS_SELECTOR, code)
code_input.send_keys("141980")

sleep(2)

button_continue = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'continue')))
button_continue.click()

sleep(2)

# Read total price
total_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text

# Извлекаем только числовое значение
total_price_text = total_price.split('$')[1]  

# Close the browser
driver.quit()

# Assert total price
assert float(total_price_text.replace(',', '')) == 58.29
print(total_price_text)
