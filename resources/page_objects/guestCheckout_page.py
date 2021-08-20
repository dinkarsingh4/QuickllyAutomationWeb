import time

import gevent.select

from resources.config_methods import DataClass
from resources.locators import GuestCheckout
from resources.page_objects.base_page import BasePage
from selenium.webdriver.common.keys import Keys as K
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutWithGuest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def enterZip(self, zip):
        self.find_element(GuestCheckout.enter_zip).clear()
        self.find_element(GuestCheckout.enter_zip).send_keys(zip)

    def click_Fresh(self):
        self.click(GuestCheckout.goFresh)

    def click_Potato(self):
        # self.click(GuestCheckout.potatoImage)
        element = self.driver.find_element_by_xpath('//*[@id="img_51875"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        self.click(GuestCheckout.AddtoCart)

    def click_Cart(self):
        self.click(GuestCheckout.Cart)

    def click_Checkout(self):
        self.click(GuestCheckout.checkout)

    def click_guestLogin(self):
        self.click(GuestCheckout.guest)

    def Enter_Name(self, fname):
        self.find_element(GuestCheckout.Fname).clear()
        self.find_element(GuestCheckout.Fname).send_keys(fname)

    def Enter_Name2(self, lname):
        self.find_element(GuestCheckout.Lname).clear()
        self.find_element(GuestCheckout.Lname).send_keys(lname)

    def EnterAddress(self, add):
        self.find_element(GuestCheckout.Address).clear()
        self.find_element(GuestCheckout.Address).send_keys(add)
        time.sleep(5)
        self.find_element(GuestCheckout.Address).send_keys(K.ARROW_DOWN)
        self.find_element(GuestCheckout.Address).send_keys(K.ENTER)

    def EnterNumber(self, num):
        self.find_element(GuestCheckout.number).clear()
        self.find_element(GuestCheckout.number).send_keys(num)

    def Enter_email(self, mail):
        self.find_element(GuestCheckout.email).clear()
        self.find_element(GuestCheckout.email).send_keys(mail)

    def click_submit(self):
        self.click(GuestCheckout.submit)

    def click_SubmitZip(self):
        self.click(GuestCheckout.submit_zip)

    def click_checkout2(self):
        self.click(GuestCheckout.checkout2)



