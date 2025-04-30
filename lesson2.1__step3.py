from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = input.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Ваш код, который заполняет обязательные поля
    input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_field.send_keys(calc(x))
    input_radiobutton = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
    input_radiobutton.click()
    input_checkbox = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
    input_checkbox.click()
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    # input_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    # input_email.send_keys("lalala@gmail.com")
    # Отправляем заполненную форму
    # button = browser.find_element(By.XPATH, "//button[@type='submit']")
    # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
