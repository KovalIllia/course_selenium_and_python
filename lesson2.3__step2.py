import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    first_button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    first_button.click()
    allert_window = browser.switch_to.alert
    allert_window.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text

    input_field = browser.find_element(By.XPATH, "//input[@class='form-control']")
    input_field.send_keys(calc(x))
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()
