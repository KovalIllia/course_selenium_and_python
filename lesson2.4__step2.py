import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100")
    )
    book_button = browser.find_element(By.XPATH, "//button[@id='book']").click()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


    # message = browser.find_element(By.XPATH, "//h5[@id='price']")

    # assert "$100" in message.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    input_field = browser.find_element(By.XPATH, "//input[@class='form-control']")
    input_field.send_keys(calc(x))
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()
