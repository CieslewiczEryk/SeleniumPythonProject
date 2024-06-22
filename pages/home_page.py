from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


class Locators:
    """Lokatory na glownej stronie"""
    LOGIN_LINK = (By.ID, "login-button")


class HomePage(BasePage):
    """Strona glowna"""
    def click_log_in(self):
        """kliknij przycisk Log in i wroc do strony logowania"""
        el = self.driver.find_element(*Locators.LOGIN_LINK)
        el.click()
        return LoginPage(self.driver)
