from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#options = webdriver.ChromeOptions() # у меня возникает ошибка, говорящая о блокировке сайта. Поэтому такая заплатка.
#options.add_argument('--ignore-ssl-errors=yes')
#options.add_argument('--ignore-certificate-errors')

# создаем новый экземпляр двайвера
driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# прописываем драйвер ожидания
driver.implicitly_wait(20)

# запускаем сайт и кликаем на кнопку
driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()


# выводим текст из зеленой плашки.
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()