# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from resources.config_methods import DataClass
from resources.locators import MiniCart
from resources.page_objects.base_page import BasePage
# from selenium.common.exceptions import WebDriverException
# import time


class Cart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterEmail(self, email):
        self.find_elements(MiniCart.Email).clear()
        self.find_element(MiniCart.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(MiniCart.Pass).clear()
        self.find_element(MiniCart.Pass).send_keys(password)

    def click_login(self):
        self.click(MiniCart.LoginButton)

    def click_signin(self):
        self.scroll_to_element(MiniCart.SignInButton)
        self.click(MiniCart.SignInButton)

    def zip(self, zipcode):
        # self.scroll_to_element(MiniCart.enter_zip)
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

    # def click_select(self):
    #     # self.scroll_to_element(MiniCart.select_button1)
    #     self.click(MiniCart.select_button1)
    #
    # def click_select2(self):
    #     self.scroll_to_element(MiniCart.select_button2)
    #     self.click(MiniCart.select_button2)
    #
    # def click_select3(self):
    #     self.scroll_to_element(MiniCart.select_button3)
    #     self.click(MiniCart.select_button3)

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

    def click_Checkout(self):
        self.click(MiniCart.proceed_to_checkOut)

    def click_additem(self):
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchhide"]/div[8]/div/div/div[1]/div/div/div/div[5]/div/a'))).click()
        # self.scroll_to_element(MiniCart.additem)
        self.driver.implicitly_wait(60)
        self.click(MiniCart.additem)
        # self.driver.execute_script(MiniCart.additem)

    def click_AddItem1(self):
        self.scroll_to_element(MiniCart.additem2)
        self.driver.implicitly_wait(20)
        self.click(MiniCart.additem2)

    def click_order(self):
        self.click(MiniCart.orderFood)

    def click_express(self):
        self.click(MiniCart.express)

    def click_item(self):
        self.scroll_to_element(MiniCart.item1)
        self.click(MiniCart.item1)

    def click_additem1(self):
        # self.scroll_to_element(MiniCart.additem1)
        self.click(MiniCart.additem1)

    def click_Additem2(self):
        self.click(MiniCart.addToCart)
