from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Firefox(options=options)

#Откройте страницу 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")

sleep(3)

for i in range(3):
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
    blue_button.click()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.quit()


