from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys


# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Переход на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Дожидаемся загрузки всех картинок
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Done')]")))


    # Получаем значение атрибута src у 3-й картинки
image_src = "#award"
image_src = driver.find_element(By.CSS_SELECTOR, image_src).get_attribute('src')

    # Выводим значение в консоль
print(image_src)


    # Закрываем браузер
driver.quit()

#<img id="award" alt="award" src="img/award.png">