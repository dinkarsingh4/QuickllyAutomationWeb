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
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianGrocery(self):
        self.driver.implicitly_wait(20)
        self.scroll_to_element(IndianGroceryBox.indianGrocery)
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[5]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(IndianGroceryBox.indianGrocery)

    def click_weekly(self):
        self.click(IndianGroceryBox.weekly)

    def click_Biweekly(self):
        self.click(IndianGroceryBox.BiWeekly)

    def click_Monthly(self):
        self.click(IndianGroceryBox.Monthly)

    def click_Once(self):
        self.click(IndianGroceryBox.Once)

    def click_buildABox(self):
        self.click(IndianGroceryBox.buildABox)

    def click_OIG(self):
        self.click(IndianGroceryBox.OIG)
