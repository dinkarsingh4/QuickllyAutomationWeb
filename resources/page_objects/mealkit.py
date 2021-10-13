from resources.config_methods import DataClass
from resources.locators import MealKit
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Meal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(MealKit.enter_zip).clear()
        self.find_element(MealKit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(MealKit.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector('#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_popular(self):
        element = self.driver.find_element_by_xpath('//*[@id="profile-tab"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.popular)

    def click_new(self):
        element = self.driver.find_element_by_xpath('//*[@id="home-tab"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.new)

    def click_grocery(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[1]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.groceries)

    def click_food(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[2]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.food)

    def click_catering(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[3]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.catering)

    def click_mealBasket(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[4]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.mealbasket)

    def click_tiffin(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[5]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.tiffin)

    def click_mealKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[6]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.mealKit)

    def click_instant(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[7]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.instantPot)

    def click_recipes(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[8]/a/div/div[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.recipes)

    def click_organic(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[9]/a/div/div/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.organic)

    def click_chai(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[10]/a/div/div/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.chai)

    def click_indianMeal(self):
        element = self.driver.find_element_by_xpath('//*[@id="myTabContent"]/div[6]/div[11]/a/div/div/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.indianMealKit)

    def click_home(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.home)

    def click_home1(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div/div/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(MealKit.home)

    def click_home2(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="store-lising-main-bread-crumb"]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_home3(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[6]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_home4(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="nav-tabContent"]/div[1]/ul/li[1]/a')
        self.driver.execute_script("arguments[0].click();", element)



