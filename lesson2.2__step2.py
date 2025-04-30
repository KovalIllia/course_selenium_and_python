import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")

    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(calc(x))
    checkbox_field = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
    checkbox_field.click()
    radiobutton_field = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
    radiobutton_field.click()
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()


finally:
    time.sleep(10)

    browser.quit()
