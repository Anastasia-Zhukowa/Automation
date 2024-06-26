import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.ShopPage import LoginPage
from pages.ShopPage import ShopPage
from pages.ShopPage import CheckoutPage



# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)
    checkout_page = CheckoutPage(driver)
    
    login_page.open_url("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    shop_page.add_items_to_cart()
    checkout_page.checkout("Anastasia", "Zhukova", "141980")

    txt = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))).text
    driver.quit()
    assert txt == "Total: $58.29"