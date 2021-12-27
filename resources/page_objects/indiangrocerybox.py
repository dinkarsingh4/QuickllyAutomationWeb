from resources.config_methods import DataClass
from resources.locators import IndianGroceryBox
from resources.page_objects.base_page import BasePage


class IndianGrocery(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(IndianGroceryBox.enter_zip).clear()
        self.find_element(IndianGroceryBox.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(IndianGroceryBox.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(12) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianGrocery(self):
        self.driver.implicitly_wait(20)
        self.scroll_to_element(IndianGroceryBox.indianGrocery)
        element = self.driver.find_element_by_css_selector('#home > div > div:nth-child(6) > div > a > div > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_OIG(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)
