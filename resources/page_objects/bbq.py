from resources.config_methods import DataClass
from resources.locators import BBQ
from resources.page_objects.base_page import BasePage

class BBQKIT(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(BBQ.enter_zip).clear()
        self.find_element(BBQ.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(BBQ.submit_zip)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(11) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_bbqKit(self):
        element = self.driver.find_element_by_css_selector('#home > div > div:nth-child(10) > div > a > div > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AllGrills(self):
        self.click(BBQ.AllGrills)

    def click_VegGrills(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[3]/ul/li[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_NonVeg(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[3]/ul/li[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartVeggie(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[1]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartTikka(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[2]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartReshmi(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[3]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartAloo(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[4]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartHariyaliChicken(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[5]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartHariyaliPaneer(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[6]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartPaneerTikka(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[7]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartTandooriChicken(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[8]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartLamb(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[9]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def AddToCartBoti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[10]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_five(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[4]/div/div[1]/div[2]/ul/li[2]/label/input')
        self.driver.execute_script("arguments[0].click();", element)

    def click_eight(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[2]/div[4]/div/div[1]/div[2]/ul/li[1]/label/input')
        self.driver.execute_script("arguments[0].click();", element)
