import time

from resources.config_methods import DataClass
from resources.locators import Refer
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReferAFriend(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_refer(self):
        self.click(Refer.refer)

    def click_referLink(self):
        self.click(Refer.referLink)

    def click_facebook(self):
        # time.sleep(30)
        element = self.driver.find_element_by_css_selector('#referfb')
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Refer.clickFacebook)).click()
        # self.click(Refer.clickFacebook)

    def click_facebookLink(self):
        element = self.driver.find_element_by_xpath('//*[@id="shareonFacebookBtn"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Refer.facebookLink)

    def click_twitter(self):
        element = self.driver.find_element_by_xpath('//*[@id="refertw"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Refer.clickTwitter)

    def click_twitterLink(self):
        element = self.driver.find_element_by_xpath('//*[@id="shareonTwitterBtn"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Refer.twitterLink)
