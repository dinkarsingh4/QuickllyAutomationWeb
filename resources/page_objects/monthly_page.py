from resources.config_methods import DataClass
from resources.locators import Monthly
from resources.page_objects.base_page import BasePage


class MONTHLY(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Monthly.enter_zip).clear()
        self.find_element(Monthly.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Monthly.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NationWideShop(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(5) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSweet(self):
        self.click(Monthly.indianSweet)

    def click_buildABox(self):
        self.click(Monthly.buildAbox)

    def click_addMasalaMathai(self):
        self.click(Monthly.addMasalaMathai)

    def click_plusMasalaMathai(self):
        self.click(Monthly.plusMasalaMathai)

    def click_addToCartMasala(self):
        self.click(Monthly.AddToCart)

    def click_Cart(self):
        self.click(Monthly.Cart)

    def click_Checkout(self):
        self.click(Monthly.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(Monthly.Pay)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(Monthly.Email).clear()
        self.find_element(Monthly.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Monthly.Pass).clear()
        self.find_element(Monthly.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_monthly(self):
        self.click(Monthly.Monthly)
