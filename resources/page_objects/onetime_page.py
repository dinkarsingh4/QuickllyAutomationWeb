from resources.config_methods import DataClass
from resources.locators import OneTime
from resources.page_objects.base_page import BasePage

class ONETIME(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(OneTime.enter_zip).clear()
        self.find_element(OneTime.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(OneTime.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NationWideShop(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(6) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSweet(self):
        self.click(OneTime.indianSweet)

    def click_buildABox(self):
        self.click(OneTime.buildAbox)

    def click_addMasalaMathai(self):
        self.click(OneTime.addMasalaMathai)

    def click_plusMasalaMathai(self):
        self.click(OneTime.plusMasalaMathai)

    def click_addToCartMasala(self):
        self.click(OneTime.AddToCart)

    def click_Cart(self):
        self.click(OneTime.Cart)

    def click_Checkout(self):
        self.click(OneTime.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(OneTime.Pay)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(OneTime.Email).clear()
        self.find_element(OneTime.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(OneTime.Pass).clear()
        self.find_element(OneTime.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)