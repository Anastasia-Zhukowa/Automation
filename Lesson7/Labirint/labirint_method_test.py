
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait



cookie = {"name": "cookie_policy", "value": "1"}

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def open_labirint():
    # перейти на сайт Лабиринта
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    # Найти все книги по слову 
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def add_books():
    # Добавить все книги на первой странице в корзину и посчитать

    buy_buttons = browser.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter

def go_to_cart():
    # Перейти в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # Получить текущее значение
    txt = browser.find_element(
        By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
    return int(txt)

def close_driver():
    browser.quit()


def test_card_counter():
    open_labirint()
    search('python')
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()
    assert added == cart_counter

def test_empty_search():
    open_labirint()
    search("no book search term")
    txt = browser.find_element(
        By.CSS_SELECTOR, "div.search-error").find_element(By.CSS_SELECTOR, 'h1').text
    assert txt == "Мы ничего не нашли по вашему запросу! Что делать?"
    close_driver()
