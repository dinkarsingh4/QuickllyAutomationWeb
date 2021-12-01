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
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[4]/img')
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
            '/html/body/div[5]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)