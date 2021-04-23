from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from resources.config_methods import DataClass
from resources.locators import MiniCart
from resources.page_objects.base_page import BasePage
# from selenium.common.exceptions import WebDriverException
# import time


class Cart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.scroll_to_element(MiniCart.enter_zip)
        self.find_elements(MiniCart.enter_zip).clear()
        self.find_element(MiniCart.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.scroll_to_element(MiniCart.submit_zip)
        self.click(MiniCart.submit_zip)

    def click_MiniCart(self):
        # WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(MiniCart.click_cart)).click()
        self.scroll_to_element(MiniCart.click_cart)
        self.click(MiniCart.click_cart)

    def Empty_cart(self):
        self.find_element(MiniCart.empty_cart).get_attribute('innerHTML')

    def click_CheckOut(self):
        self.click(MiniCart.proceed_to_checkOut)

    def click_select(self):
        # self.scroll_to_element(MiniCart.select_button)
        self.click(MiniCart.select_button)

    def click_AddToCart(self):
        self.scroll_to_element(MiniCart.Add1)
        self.click(MiniCart.Add1)

    def click_plus(self):
        self.scroll_to_element(MiniCart.PlusQuantity)
        self.click(MiniCart.PlusQuantity)

    def click_minus(self):
        self.scroll_to_element(MiniCart.MinusQuantity)
        self.click(MiniCart.MinusQuantity)

    def click_delete(self):
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MiniCart.delete_item)).click()
        self.click(MiniCart.delete_item)
