from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go_to_page(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    def set_delay(self, delay: str):
        delay_element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_number(self, number: str):
        self.driver.find_element(By.XPATH, f"//div[@class='keys']/span[text()='{number}']").click()

    def click_operator(self, operator: str):
        self.driver.find_element(By.XPATH, f"//div[@class='keys']/span[text()='{operator}']").click()

    def get_result(self) -> str:
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text