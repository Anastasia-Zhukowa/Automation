from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



#Откройте страницу http://uitestingplayground.com/dynamicid
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")



for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    blue_button.click()

sleep(2)

driver.quit()

