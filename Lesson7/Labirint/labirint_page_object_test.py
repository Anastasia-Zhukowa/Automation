from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from Lesson7.Labirint.pages.MainPage import MainPage
from Lesson7.Labirint.pages.ResultPage import ResultPage
from Lesson7.Labirint.pages.CartPage import CartPage


def test_card_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('python')

    result_page = ResultPage(browser)
    to_be = result_page.add_books()

    sleep(5)


    cart_page = CartPage(browser)
    cart_page.get() #Переход на страницу с корзиной
    as_is = cart_page.get_counter() #Текущее значение счетчика на странице 

    sleep(5)

    assert as_is == to_be #Сравниваем значения счетчика с вернувшимся кол-вом книг
    sleep(5)
    browser.quit()

def test_empty_search():
    browser = webdriver.Chrome()
    main_page = MainPage(browser) 
    main_page.set_cookie_policy()
    main_page.search("no book search term")

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()
    assert msg == "Мы ничего не нашли по вашему запросу! Что делать?"
    browser.quit()