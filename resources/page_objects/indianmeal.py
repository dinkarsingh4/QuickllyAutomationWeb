from resources.config_methods import DataClass
from resources.locators import IndianMealKit
from resources.page_objects.base_page import BasePage


class IndianMeal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(IndianMealKit.enter_zip).clear()
        self.find_element(IndianMealKit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(IndianMealKit.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[6]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianMealKit(self):
        self.click(IndianMealKit.indianmealKit)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[2]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[2]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Monthly2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectProduct(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectProduct2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_IMKS(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[1]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)
