from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/simple_form_find_task.html"
result = str(math.ceil(math.pow(math.pi, math.e) * 10000))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    input_first_page = browser.find_element(By.PARTIAL_LINK_TEXT, result)
    input_first_page.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Illia")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Koval")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("London")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Great Britain")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
