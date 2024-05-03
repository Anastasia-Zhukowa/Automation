from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.FormPage import FormPage # импортируем класс 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # запускаем драйвер. Если делать по аналогии с лабиринтом, то он должен быть в функции ниже.

def test_form_elements(): # здесь уже вносим данные, в первой строчке указываем какой драйвер запускаем
    form_page = FormPage(driver)
    
    form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+79030655987", "Москва", "Россия", "QA", "SkyPro")

    zip_code_color = form_page.check_form_field_color("zip-code") # с этой строкой я еще похимичу,зможно, получится ее часть перенести в Класс. 
    assert zip_code_color == "rgba(248, 215, 218, 1)"
    other_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field in other_fields:
        field_color = form_page.check_form_field_color(field)
        assert field_color == "rgba(209, 231, 221, 1)"

    driver.quit()