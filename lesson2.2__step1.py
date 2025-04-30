import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    first_value = browser.find_element(By.XPATH, "//span[@id='num1']").text
    second_value = browser.find_element(By.XPATH, "//span[@id='num2']").text
    result = int(first_value) + int(second_value)
    list_field = browser.find_element(By.XPATH, "//select[@id='dropdown']").click()
    list_field_value = browser.find_element(By.XPATH, f"//select[@id='dropdown']//option[@value={result}]").click()
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']").click()


finally:
    time.sleep(10)

    browser.quit()
