from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


def test_registration1():
    browser = webdriver.Chrome()
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Заповнення обов'язкових полів
        input_first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input_first_name.send_keys("Kla")
        input_last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input_last_name.send_keys("Kla")
        input_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input_email.send_keys("lalala@gmail.com")

        # Відправляємо заповнену форму
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        # Перевіряємо, що змогли зареєструватися
        # чекаємо завантаження сторінки
        time.sleep(1)

        # знаходимо елемент, що містить текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записуємо в змінну welcome_text текст із елементу welcome_text_elt
        welcome_text = welcome_text_elt.text

        # перевіряємо, що очікуваний текст збігається з текстом на сторінці сайту
        assert welcome_text == "Congratulations! You have successfully registered!"

    finally:
        # затримка для візуальної оцінки результатів
        time.sleep(1)
        # закриваємо браузер після всіх маніпуляцій
        browser.quit()


def test_registration2():
    browser = webdriver.Chrome()
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        # Заповнення обов'язкових полів
        input_first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
        input_first_name.send_keys("Kla")
        # input_last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        # input_last_name.send_keys("Kla")
        input_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input_email.send_keys("lalala@gmail.com")

        # Відправляємо заповнену форму
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()

        # Перевіряємо, що змогли зареєструватися
        # чекаємо завантаження сторінки
        time.sleep(1)

        # знаходимо елемент, що містить текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записуємо в змінну welcome_text текст із елементу welcome_text_elt
        welcome_text = welcome_text_elt.text

        # перевіряємо, що очікуваний текст збігається з текстом на сторінці сайту
        assert welcome_text == "Congratulations! You have successfully registered!"

    finally:
        # затримка для візуальної оцінки результатів
        time.sleep(1)
        # закриваємо браузер після всіх маніпуляцій
        browser.quit()

if __name__ == "__main__":
    pytest.main()