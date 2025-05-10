import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

data = {"login_stepik": "cheknoldas92@gmail.com",
        "password_stepik": "Qwerty11"}
with open("config.json", "w") as f:
    json.dump(data, f)

# створення json
@pytest.fixture(scope="session")
def load_config():
    with open("config.json", "r") as config_file:
        config=json.load(config_file)
        return config

# фікстура для запуску browser
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLogin():
    def test_autorization(self,browser,load_config):
        login=load_config["login_stepik"]
        password=load_config["password_stepik"]
        browser.implicitly_wait(5)
        browser.get("https://stepik.org/lesson/236895/step/1")
        login_button=browser.find_element(By.XPATH,"//a[@class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']").click()
        email_button=browser.find_element(By.XPATH,"//input[@id='id_login_email']").send_keys(login)
        password_button=browser.find_element(By.XPATH,"//input[@id='id_login_password']").send_keys(password)
        submit_button=browser.find_element(By.XPATH,"//button[@class='sign-form__btn button_with-loader ']").click()
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")
