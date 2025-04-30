import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # добавляем к этому пути имя файла
    # element.send_keys(file_path)

    first_name = browser.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.send_keys("Illia")
    last_name = browser.find_element(By.XPATH, "//input[@name='lastname']")
    last_name.send_keys("Koval")
    email_field = browser.find_element(By.XPATH, "//input[@name='email']")
    email_field.send_keys("koval@yahoo.com")
    current_dir = os.path.abspath(os.path.dirname(
        "/home/koval_i/Documents/MyPythonProjects/lesson2.2_step3.py"))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'homework.txt')
    upload_file_field = browser.find_element(By.XPATH, "//input[@type='file']")
    upload_file_field.send_keys(file_path)
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()
