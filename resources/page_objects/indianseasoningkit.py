from resources.config_methods import DataClass
from resources.locators import IndianSeasoningKit
from resources.page_objects.base_page import BasePage


class Indian(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(IndianSeasoningKit.enter_zip).clear()
        self.find_element(IndianSeasoningKit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(IndianSeasoningKit.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(12) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSeasoning(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[5]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[1]/center/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[1]/center/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[1]/center/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[1]/center/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly2(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[2]/center/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly2(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[2]/center/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly2(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[2]/center/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once2(self):
        element = self.driver.find_element_by_xpath('//*[@id="seasn1"]/div[2]/center/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectProduct(self):
        element = self.driver.find_element_by_css_selector('#seasonings-kit > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectProduct2(self):
        element = self.driver.find_element_by_xpath('//*[@id="easyindebowl"]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_ISK(self):
        element = self.driver.find_element_by_xpath('/html/body/div[8]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_redHotChilli(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div/div[1]/div[5]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(IndianSeasoningKit.Email).clear()
        self.find_element(IndianSeasoningKit.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(IndianSeasoningKit.Pass).clear()
        self.find_element(IndianSeasoningKit.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(IndianSeasoningKit.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(IndianSeasoningKit.Pay)

    def click_quicklly(self):
        self.click(IndianSeasoningKit.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)
