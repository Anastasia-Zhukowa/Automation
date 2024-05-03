from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

# Клик по кнопке. Chrome
# Откройте страницу
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(5)

# Пять раз кликните на кнопку "Add Element"
for i in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

sleep(2)

# Соберите со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

sleep(5)

# Выведите на экран размер списка
print(len(delete_buttons))

sleep(5)