from resources.config_methods import DataClass
from resources.locators import Coupon
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class evoucher(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterZipcode(self, zip):
        self.find_elements(Coupon.zipCode).clear()
        self.find_element(Coupon.zipCode).send_keys(zip)

    def ClickSubmit(self):
        self.click(Coupon.submitButton)

    def select_dropdown(self):
        self.click(Coupon.yourAccount)

    def click_signin(self):
        self.scroll_to_element(Coupon.SignInButton)
        self.click(Coupon.SignInButton)

    def EnterEmail(self, email):
        self.find_elements(Coupon.Email).clear()
        self.find_element(Coupon.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Coupon.Pass).clear()
        self.find_element(Coupon.Pass).send_keys(password)

    def click_login(self):
        self.click(Coupon.LoginButton)

    def click_additem(self):
        self.scroll_to_element(Coupon.additem)
        self.click(Coupon.additem)

    def click_AddItem1(self):
        self.click(Coupon.additem2)

    def click_MiniCart(self):
        self.scroll_to_element(Coupon.click_cart)
        self.click(Coupon.click_cart)

    def click_Checkout(self):
        self.click(Coupon.proceed_to_checkOut)

    def EnterEvoucher(self, evoucher):
        self.find_elements(Coupon.evoucher_text_box).clear()
        self.find_element(Coupon.evoucher_text_box).send_keys(evoucher)

    def click_apply(self):
        self.scroll_to_element(Coupon.Apply)
        element = self.driver.find_element_by_xpath('//*[@id="parRadioOne"]/a')
        self.driver.execute_script("arguments[0].click();", element)
