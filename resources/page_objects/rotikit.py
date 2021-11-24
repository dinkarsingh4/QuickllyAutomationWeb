from resources.config_methods import DataClass
from resources.locators import RotiKit
from resources.page_objects.base_page import BasePage


class RotiBox(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(RotiKit.enter_zip).clear()
        self.find_element(RotiKit.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(RotiKit.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_rotiKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[6]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_weekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[2]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Biweekly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[3]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(RotiKit.BiWeekly)

    def click_Monthly(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[4]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Once(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[2]/ul/li[1]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_WholeWheat(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[1]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_roti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[2]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_multiGrain(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[3]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_rotla(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[4]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Paratha(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[5]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_SpecialRoti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[2]/div[2]/div/div[6]/a/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Bakhri(self):
        element = self.driver.find_element_by_css_selector('#searchhide > section.clsFoodStores.organicproductsection.rotikalandingpage.clsPgWidth > div.tabcontents > div > div:nth-child(7) > a > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_OrderRotiKit(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[1]/div/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_buildABox(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)
