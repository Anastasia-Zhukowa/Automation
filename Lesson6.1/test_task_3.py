from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    yield driver
    sleep(2)

def test_shopping(driver):
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
    password_input = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce") 
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
    add_backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    add_tshirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    add_onesie = driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie").click()
    cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "shopping_cart_container")))
    cart_button.click()

    checkout =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'checkout')))
    checkout.click()

    first_name_input = driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Anastasia")

    last_name_input = driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Zhukova")

    code_input  = driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("141980")

    button_continue = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'continue')))
    button_continue.click()


    # Read total price
    total_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text

    # Извлекаем только числовое значение
    total_price_text = total_price.split('$')[1]  

    # Close the browser
    driver.quit()

# Assert total price
    assert float(total_price_text.replace(',', '')) == 58.29
    print(total_price_text)
