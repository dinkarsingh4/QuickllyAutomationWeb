from resources.config_methods import DataClass
from resources.locators import IndianMealKitAndSauces
from resources.page_objects.base_page import BasePage


class Sauces(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(IndianMealKitAndSauces.enter_zip).clear()
        self.find_element(IndianMealKitAndSauces.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(IndianMealKitAndSauces.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(12) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_sauces(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[9]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_BayArea(self):
        self.click(IndianMealKitAndSauces.BayArea)

    def click_NationWide(self):
        self.click(IndianMealKitAndSauces.nationwide)

    def click_select(self):
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_select1(self):
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_backToPage(self):
        self.click(IndianMealKitAndSauces.backToPage)

    def click_Eat(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Vegetarian(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Vegan(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Nut(self):
        element = self.driver.find_element_by_xpath('//*[@id="bay-shop"]/div[2]/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Bay(self):
        self.click(IndianMealKitAndSauces.clickBay)