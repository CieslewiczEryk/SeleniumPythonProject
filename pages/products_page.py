from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class Locators:
    """Lokatory strony proguktow"""
    PRODUCT = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    # BACKPACK
    BACKPACK_ADD = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    BACKPACK = (By.XPATH, '//*[@id="item_4_title_link"]')
    BACKPACK_FIRST_NAME = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    BACKPACK_SECOND_NAME = By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
    BACKPACK_FIRST_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    BACKPACK_SECOND_PRICE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
    # LIGHT
    LIGHT_ADD = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    LIGHT_FIRST_NAME = (By.XPATH, '//*[@id="item_0_title_link"]/div')
    LIGHT_SECOND_NAME = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    LIGHT_FIRST_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
    LIGHT_SECOND_PRICE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
    # TSHIRT
    TSHRT_FIRST_NAME = (By.XPATH, '//*[@id="item_1_title_link"]/div')
    TSHRT_SECOND_NAME = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    TSHRT_FIRST_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
    TSHRT_SECOND_PRICE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
    TSHIRT_ADD = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    # JACKET
    JACKET_FIRST_NAME = (By.XPATH, '//*[@id="item_5_title_link"]/div')
    JACKET_SECOND_NAME = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    JACKET_FIRST_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
    JACKET_SECOND_PRICE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
    JACKET_ADD = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    # ONESIE
    ONESIE_FIRST_NAME = (By.XPATH, '//*[@id="item_2_title_link"]/div')
    ONESIE_SECOND_NAME = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    ONESIE_FIRST_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div')
    ONESIE_SECOND_PRICE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
    ONESIE_ADD = (By.ID, 'add-to-cart-sauce-labs-onesie')
    # TSHIRT_RED
    TSHIRT_RED_FIRST_NAME = (By.XPATH, '//*[@id="item_3_title_link"]/div')
    TSHIRT_RED_SECOND_NAME = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    TSHIRT_RED_FIRST_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
    TSHIRT_RED_SECOND_PRICE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')
    TSHIRT_RED_ADD = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    NUMBER = (By. XPATH, '//*[@id="shopping_cart_container"]/a/span')


class ItemsIDs:
    backpack_ID = 'id=4'
    light_ID = 'id=0'
    tshirt_ID = 'id=1'
    jacket_ID = 'id=5'
    onesie_ID = 'id=2'
    tshirt_red_ID = 'id=3'



class ProductsPage(BasePage):

    def title(self):
        el = self.driver.find_element(*Locators.PRODUCT)
        return el.text

    def add_product(self):
        """dodawanie produktu do koszyka"""
        backpack = self.driver.find_element(*Locators.BACKPACK_ADD)
        backpack.click()
        light = self.driver.find_element(*Locators.LIGHT_ADD)
        light.click()
        tshirt = self.driver.find_element(*Locators.TSHIRT_ADD)
        tshirt.click()
        jacket = self.driver.find_element(*Locators.JACKET_ADD)
        jacket.click()
        onesie = self.driver.find_element(*Locators.ONESIE_ADD)
        onesie.click()
        tshirtred = self.driver.find_element(*Locators.TSHIRT_RED_ADD)
        tshirtred.click()

    def produckts_number(self):
        number = self.driver.find_element(*Locators.NUMBER)
        return number.text

    def backpack_first_name(self):
        first_name = self.driver.find_element(*Locators.BACKPACK_FIRST_NAME)
        return first_name.text

    # Backpack
    def backpack(self):
        backpack = self.driver.get("https://www.saucedemo.com/inventory-item.html?" + ItemsIDs.backpack_ID)
        return backpack

    def backpack_second_name(self):
        second_name = self.driver.find_element(*Locators.BACKPACK_SECOND_NAME)
        return second_name.text

    def backpack_first_price(self):
        price = self.driver.find_element(*Locators.BACKPACK_FIRST_PRICE)
        return price.text

    def backpack_second_price(self):
        price = self.driver.find_element(*Locators.BACKPACK_SECOND_PRICE)
        return price.text

    # Light
    def light_first_name(self):
        first_name = self.driver.find_element(*Locators.LIGHT_FIRST_NAME)
        return first_name.text

    def light(self):
        light = self.driver.get("https://www.saucedemo.com/inventory-item.html?" + ItemsIDs.light_ID)
        return light

    def light_second_name(self):
        second_name = self.driver.find_element(*Locators.LIGHT_SECOND_NAME)
        return second_name.text

    def light_first_price(self):
        price = self.driver.find_element(*Locators.LIGHT_FIRST_PRICE)
        return price.text

    def light_second_price(self):
        price = self.driver.find_element(*Locators.LIGHT_SECOND_PRICE)
        return price.text

    # Tshirt
    def tshirt_first_name(self):
        first_name = self.driver.find_element(*Locators.TSHRT_FIRST_NAME)
        return first_name.text

    def tshirt(self):
        tshirt = self.driver.get("https://www.saucedemo.com/inventory-item.html?" + ItemsIDs.tshirt_ID)
        return tshirt

    def tshirt_second_name(self):
        second_name = self.driver.find_element(*Locators.TSHRT_SECOND_NAME)
        return second_name.text

    def tshirt_first_price(self):
        price = self.driver.find_element(*Locators.TSHRT_FIRST_PRICE)
        return price.text

    def tshirt_second_price(self):
        price = self.driver.find_element(*Locators.TSHRT_SECOND_PRICE)
        return price.text

    # Jacket
    def jacket_first_name(self):
        first_name = self.driver.find_element(*Locators.JACKET_FIRST_NAME)
        return first_name.text

    def jacket(self):
        jacket = self.driver.get("https://www.saucedemo.com/inventory-item.html?" + ItemsIDs.jacket_ID)
        return jacket

    def jacket_second_name(self):
        second_name = self.driver.find_element(*Locators.JACKET_SECOND_NAME)
        return second_name.text

    def jacket_first_price(self):
        price = self.driver.find_element(*Locators.JACKET_FIRST_PRICE)
        return price.text

    def jacket_second_price(self):
        price = self.driver.find_element(*Locators.JACKET_SECOND_PRICE)
        return price.text

    # ONESIE
    def onesie_first_name(self):
        first_name = self.driver.find_element(*Locators.ONESIE_FIRST_NAME)
        return first_name.text

    def onesie(self):
        onesie = self.driver.get("https://www.saucedemo.com/inventory-item.html?" + ItemsIDs.onesie_ID)
        return onesie

    def onesie_second_name(self):
        second_name = self.driver.find_element(*Locators.ONESIE_SECOND_NAME)
        return second_name.text

    def onesie_first_price(self):
        price = self.driver.find_element(*Locators.ONESIE_FIRST_PRICE)
        return price.text

    def onesie_second_price(self):
        price = self.driver.find_element(*Locators.ONESIE_SECOND_PRICE)
        return price.text

    # tshirt_red
    def tshirt_red_first_name(self):
        first_name = self.driver.find_element(*Locators.TSHIRT_RED_FIRST_NAME)
        return first_name.text

    def tshirt_red(self):
        tshirt_red = self.driver.get("https://www.saucedemo.com/inventory-item.html?" + ItemsIDs.tshirt_red_ID)
        return tshirt_red

    def tshirt_red_second_name(self):
        second_name = self.driver.find_element(*Locators.TSHIRT_RED_SECOND_NAME)
        return second_name.text

    def tshirt_red_first_price(self):
        price = self.driver.find_element(*Locators.TSHIRT_RED_FIRST_PRICE)
        return price.text

    def tshirt_red_second_price(self):
        price = self.driver.find_element(*Locators.TSHIRT_RED_SECOND_PRICE)
        return price.text
