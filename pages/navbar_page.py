from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class Locators:
    navbar = (By. ID, 'react-burger-menu-btn')


class NavbarPage(BasePage):

    def navbar_click(self):
        el = self.driver.find_element(*Locators.navbar)
        el.click()


