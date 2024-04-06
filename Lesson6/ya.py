from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



def make_screenshoot(driver):
    driver.maximize_window()
    driver.get('http://ya.ru')
    sleep(5)
    driver.save_screenshot('./ya.' +driver.name+'.png')
    driver.quit()

# driver.back()
# driver.forward()
# driver.refresh() 

# driver.set_window_size(640, 460)



