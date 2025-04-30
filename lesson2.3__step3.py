import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    troll_button = browser.find_element(By.XPATH, " //button[@class='trollface btn btn-primary']")
    troll_button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text

    input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_field.send_keys(calc(x))
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()
