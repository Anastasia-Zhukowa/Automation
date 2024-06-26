from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://labirint.ru")

driver.maximize_window()
sleep(2)

driver.minimize_window()
sleep(2)

# полный экран
driver.fullscreen_window()
sleep(2)

# установка размера окна
driver.set_window_size(1000, 600)

sleep(5)