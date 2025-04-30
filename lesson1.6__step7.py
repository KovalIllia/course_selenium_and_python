from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input1 = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input1.send_keys("Illia")
    input2 = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input2.send_keys("Koval")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    input3.send_keys("London")
    input4 = browser.find_element(By.XPATH, "//input[@class='form-control'][@id='country']")
    input4.send_keys("UK")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
