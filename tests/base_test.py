from selenium import webdriver
import unittest
from time import sleep
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    """Klasa bazowa kazdego testu"""

    def setUp(self):
        """Warunki wstepne kazdego testu"""
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.delete_all_cookies()
        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.home_page = HomePage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.count = ProductsPage(self.driver)
        self.backpack = ProductsPage(self.driver)


    def testTest(self):
        pass

    def tearDown(self):
        self.driver.quit()
