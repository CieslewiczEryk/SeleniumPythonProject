from selenium.webdriver.common.alert import Alert


class BasePage:
    """Klasa bazowa strony"""
    def __init__(self, driver):
        """przechwycenie sterownika przegladarki"""
        self.driver = driver
        self.alert = Alert(self.driver)
