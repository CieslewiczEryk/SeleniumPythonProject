from tests.base_test import BaseTest
from tests.test_data import CorrectUser
from pages.navbar_page import NavbarPage
from time import sleep


class NavbarTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.correct_data = CorrectUser
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.correct_data.correct_username)
        login_page.enter_password(self.correct_data.correct_password)
        login_page.click_log_in()
        navbar_click = self.navbar_page.navbar_click()

    def test_navbar_roll(self):
        "sprawdzanie rozwijania navbara"
        sleep(2)
        self.navbar_click = self.navbar_page.NavbarPage.navbar_click()
