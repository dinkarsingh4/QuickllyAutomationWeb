from resources.config_methods import DataClass
from resources.locators import ChaiAndCoffee
from resources.page_objects.base_page import BasePage


class CACD(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(ChaiAndCoffee.enter_zip).clear()
        self.find_element(ChaiAndCoffee.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(ChaiAndCoffee.submit_zip)

    def click_ChaiAndCoffee(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[9]/div/div/div/div/a[14]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_BiWeekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_once(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_backToPage(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[8]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddKimbala(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[3]/div/div/div[1]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(ChaiAndCoffee.Email).clear()
        self.find_element(ChaiAndCoffee.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(ChaiAndCoffee.Pass).clear()
        self.find_element(ChaiAndCoffee.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(ChaiAndCoffee.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(ChaiAndCoffee.Pay)

    def click_quicklly(self):
        self.click(ChaiAndCoffee.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)
