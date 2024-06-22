from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    """Lokatory strony logowania"""
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOG_IN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By. XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')


class LoginPage(BasePage):
    def enter_username(self, username):
        """wprowadzanie nazwy uzytkownika"""
        el = self.driver.find_element(*Locators.USERNAME_INPUT)
        el.send_keys(username)

    def enter_password(self, password):
        """wprowadzanie hasla"""
        el = self.driver.find_element(*Locators.PASSWORD_INPUT)
        el.send_keys(password)

    def click_log_in(self):
        "klikniecie przycisku log in"
        self.driver.find_element(*Locators.LOG_IN_BTN).click()

    def get_error_message(self):
        """poczekanie na error i zwrocenie wiadomosci"""
        wait = WebDriverWait(self.driver, 4)
        error_msg = self.driver.find_element(*Locators.ERROR_MSG)
        return error_msg.text







