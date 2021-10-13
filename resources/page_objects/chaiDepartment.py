from resources.config_methods import DataClass
from resources.locators import ChaiAndCoffee
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[4]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        self.click(ChaiAndCoffee.weekly)

    def click_BiWeekly(self):
        self.click(ChaiAndCoffee.BiWeekly)

    def click_Monthly(self):
        self.click(ChaiAndCoffee.monthly)

    def click_once(self):
        self.click(ChaiAndCoffee.Once)

    def click_buildABox(self):
        self.click(ChaiAndCoffee.buildABox)

    def click_backToPage(self):
        self.click(ChaiAndCoffee.backToChaiCoffee)
