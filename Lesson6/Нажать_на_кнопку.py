from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


# зайти на сайта
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")


# ждать
# нажать на кнопку ajaxButton
# ждать
# вывести текст из зеленой плашки
# остановить драйвер
driver.quit()



try:
    # Ожидание появления модального окна
    botton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ajaxButton"))) 
    
    # Нахождение кнопки Close и клик по ней
    blue_button = botton.find_element(By.CSS_SELECTOR, "ajaxButton")
    blue_button = botton.find_element
    


finally:
    print("Element found:", botton.text)
    # Закрытие браузера
    driver.quit()


#driver.find_element(By.CSS_SELECTOR, 'button[type=submin]').click

#'[id="ajaxButton"]')