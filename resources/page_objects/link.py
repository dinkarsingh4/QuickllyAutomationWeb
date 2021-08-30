from resources.config_methods import DataClass
from resources.locators import Links
from resources.page_objects.base_page import BasePage



class ContactUsLinks(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_Facebook(self):
        element = self.driver.find_element_by_link_text('FACEBOOK')
        self.driver.execute_script("arguments[0].click();", element)

    def click_twitter(self):
        element = self.driver.find_element_by_link_text('TWITTER')
        self.driver.execute_script("arguments[0].click();", element)

    def click_linkedin(self):
        element = self.driver.find_element_by_link_text('LINKEDIN')
        self.driver.execute_script("arguments[0].click();", element)

    def click_youtubeLink(self):
        element = self.driver.find_element_by_link_text('YOUTUBE')
        self.driver.execute_script("arguments[0].click();", element)

    def click_instagramLink(self):
        element = self.driver.find_element_by_link_text('INSTAGRAM')
        self.driver.execute_script("arguments[0].click();", element)

    def click_pinterest(self):
        element = self.driver.find_element_by_link_text('PINTEREST')
        self.driver.execute_script("arguments[0].click();", element)
