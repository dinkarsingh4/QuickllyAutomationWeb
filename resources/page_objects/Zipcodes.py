from resources.config_methods import DataClass
from resources.locators import ZipCode
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Zip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)


    def zip(self, zipcode):
        self.find_element(ZipCode.enter_zip).clear()
        self.find_element(ZipCode.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(ZipCode.submit_zip)

    def click_quicklly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/a/img')
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(ZipCode.quicklly)).click()

    def click_department(self):
        # self.click(ZipCode.department)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[2]/div/div[1]/div[1]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_cross(self):
        self.click(ZipCode.cross)
