from resources.config_methods import DataClass
from resources.locators import Maximum
from resources.page_objects.base_page import BasePage


class MAXIMUM(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)
        
    def zip(self, zipcode):
        self.find_elements(Maximum.enter_zip).clear()
        self.find_element(Maximum.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Maximum.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NationWideShop(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(4) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSweet(self):
        self.click(Maximum.indianSweet)

    def click_buildABox(self):
        self.click(Maximum.buildAbox)

    def click_addMasalaMathai(self):
        self.click(Maximum.addMasalaMathai)

    def click_plusMasalaMathai(self):
        self.click(Maximum.plusMasalaMathai)

    def click_addToCartMasala(self):
        self.click(Maximum.AddToCart)

    def click_Cart(self):
        self.click(Maximum.Cart)

    def click_Checkout(self):
        self.click(Maximum.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(Maximum.Pay)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(Maximum.Email).clear()
        self.find_element(Maximum.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Maximum.Pass).clear()
        self.find_element(Maximum.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_monthly(self):
        self.click(Maximum.Monthly)