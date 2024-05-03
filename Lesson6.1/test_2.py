from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    #driver = webdriver.Chrome() 
    yield driver
    sleep(2)

def test_calculator(driver):
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#delay')))
    delay_input.clear()
    delay_input.send_keys('45')

    seven = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='7']")
    seven.click()
    sleep(1)
    plus = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='+']")
    plus.click()
    sleep(1)
    eight = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='8']")
    eight.click()
    sleep(1)
    equally = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='=']")
    equally.click()
    sleep(1)
    result = driver.find_element(By.CSS_SELECTOR, "div[class='screen']").text
    expected_result = '15'

    assert result == expected_result