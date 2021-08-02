from resources.config_methods import DataClass
from resources.locators import Contact
from resources.page_objects.base_page import BasePage


class contactUs(BasePage):
    """Privacy Error Page of Invisily Admin Portal"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_element(Contact.enter_zip).clear()
        self.find_element(Contact.enter_zip).send_keys(zipcode)
