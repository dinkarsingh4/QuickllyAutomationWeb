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
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianSeasoning(self):
        self.click(IndianSeasoningKit.indianSeasoning)

    def click_weekly(self):
        self.click(IndianSeasoningKit.weekly)

    def click_Biweekly(self):
        self.click(IndianSeasoningKit.BiWeekly)

    def click_Monthly(self):
        self.click(IndianSeasoningKit.Monthly)

    def click_Once(self):
        self.click(IndianSeasoningKit.Once)

    def click_weekly2(self):
        self.click(IndianSeasoningKit.weekly2)

    def click_Biweekly2(self):
        self.click(IndianSeasoningKit.BiWeekly2)

    def click_Monthly2(self):
        self.click(IndianSeasoningKit.monthly2)

    def click_Once2(self):
        self.click(IndianSeasoningKit.once2)

    def click_selectProduct(self):
        self.click(IndianSeasoningKit.selectProducts)

    def click_selectProduct2(self):
        self.click(IndianSeasoningKit.selectProducts2)

    def click_ISK(self):
        self.click(IndianSeasoningKit.clickIndian)
