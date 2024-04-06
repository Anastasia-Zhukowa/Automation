from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Переход на страницу
driver.get("http://uitestingplayground.com/textinput")

# ждем загрузку страницы 
wait = WebDriverWait(driver, 10)

# Находим поле ввода и вводим текст
form = '#newButtonName'
form_input = driver.find_element(By.CSS_SELECTOR, form)
form_input.send_keys("SkyPro")


wait = WebDriverWait(driver, 10)

blue_button = "#updatingButton"
blue_button = driver.find_element(By.CSS_SELECTOR, blue_button)
blue_button.click()

# Ждем, пока текст кнопки не изменится
wait = WebDriverWait(driver, 10)

# Получаем текст кнопки и выводим в консоль
text_button = blue_button.text
print(text_button)

# Закрываем браузер
driver.quit()
