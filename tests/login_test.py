from tests.base_test import BaseTest
from tests.test_data import TestData
from tests.test_data import CorrectUser


class LoginTest(BaseTest):
    """Testy logowania"""

    def setUp(self):
        # rozszerzam dodatkowy setup o wygenerowanie
        # danych testowych
        # wywoluje bazowy setup
        super().setUp()
        # generuje dane testowe
        self.test_data = TestData()
        self.correct_data = CorrectUser
        self.login_page = self.home_page.click_log_in()

    def test_invalid_username(self):
        """"""
        login_page = self.home_page.click_log_in()
        # wpisz niepoprawny username
        login_page.enter_username(self.test_data.user_name)
        # wpisz niepoprawne haslo
        login_page.enter_password(self.correct_data.correct_password)
        login_page.click_log_in()
        #sprawdz czy wyskakuje komunikat o niepoprawnym uzytkowniku
        self.assertEqual("Epic sadface: Username and password do not match any user in this service"
                         , login_page.get_error_message())

    def test_invalid_password(self):
        """uzywanie niepoprawnego hasla"""
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.correct_data.correct_username)
        login_page.enter_password(self.test_data.password)
        login_page.click_log_in()
        self.assertEqual("Epic sadface: Username and password do not match any user in this service"
                         , login_page.get_error_message())

    def test_invalid_username_and_password(self):
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.test_data.user_name)
        login_page.enter_password(self.test_data.password)
        login_page.click_log_in()
        self.assertEqual("Epic sadface: Username and password do not match any user in this service"
                         , login_page.get_error_message())

    def test_valid_username_and_password(self):
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.correct_data.correct_username)
        login_page.enter_password(self.correct_data.correct_password)
        login_page.click_log_in()
        self.products_page = self.products_page.title()
        self.assertEqual("Products", self.products_page.title())







