from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block &gt; div.form-group.first_class &gt; input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block &gt; div.form-group.second_class &gt; input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block &gt; div.form-group.third_class &gt; input")
    input3.send_keys("Petrov@gmail.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block &gt; div.form-group.first_class &gt; input")
    input4.send_keys("89109458877")
    input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block &gt; div.form-group.second_class &gt; input")
    input5.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
