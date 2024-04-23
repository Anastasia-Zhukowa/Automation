from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class Calculator:
    def init(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def enter_delay(self, delay_time):
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(delay_time)

    def perform_calculation(self):
        self.driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//div[@class='keys']/span[text='+']").click()
        self.driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='=']").click()

    def wait_for_result(self):
        WebDriverWait(self.driver, timeout=46).until(
            EC.text_to_be_present_in_element(locator=(By.CSS_SELECTOR, ".screen"), text_="15")
        )

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

    def close_page(self):
        self.driver.quit()