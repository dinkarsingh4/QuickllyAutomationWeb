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
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianMealKit(self):
        self.click(IndianMealKit.indianmealKit)

    def click_weekly(self):
        self.click(IndianMealKit.weekly)

    def click_Biweekly(self):
        self.click(IndianMealKit.BiWeekly)

    def click_Monthly(self):
        self.click(IndianMealKit.Monthly)

    def click_Once(self):
        self.click(IndianMealKit.Once)

    def click_weekly2(self):
        self.click(IndianMealKit.weekly2)

    def click_Biweekly2(self):
        self.click(IndianMealKit.BiWeekly2)

    def click_Monthly2(self):
        self.click(IndianMealKit.monthly2)

    def click_Once2(self):
        self.click(IndianMealKit.once2)

    def click_selectProduct(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[1]/div/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(IndianMealKit.selectProducts)

    def click_selectProduct2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/section[1]/div/div/div[2]/div/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(IndianMealKit.selectProducts2)

    def click_IMKS(self):
        self.click(IndianMealKit.IMKS)
