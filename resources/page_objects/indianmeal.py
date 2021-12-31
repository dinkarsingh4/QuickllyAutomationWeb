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
        element = self.driver.find_element_by_id('zipsubmitbtn')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > i.right.slick-arrow > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MealKit(self):
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_css_selector(
            '#searchhide > div.grocerySpecialSlider.clsFoodSpl > div > div > div > div > a:nth-child(12) > img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_indianMealKit(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="home"]/div/div[3]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

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

    def select_dropdown(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)

    def click_signin(self):
        element = self.driver.find_element_by_css_selector('#procedcheckoutBtn')
        self.driver.execute_script("arguments[0].click();", element)

    def EnterEmail(self, email):
        self.find_elements(IndianMealKit.Email).clear()
        self.find_element(IndianMealKit.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(IndianMealKit.Pass).clear()
        self.find_element(IndianMealKit.Pass).send_keys(password)

    def click_login(self):
        element = self.driver.find_element_by_xpath('//*[@id="btn-login"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(IndianMealKit.checkout)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(IndianMealKit.Pay)

    def click_quicklly(self):
        self.click(IndianMealKit.quicklly)

    def click_Checkout2(self):
        element = self.driver.find_element_by_xpath('//*[@id="dvFoodSuggestPopup"]/div/div/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBhindiMasala(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[3]/div/div/div[1]/div[1]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def plusBhindiMasala(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[3]/div/div/div[1]/div[1]/div[3]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="searchhide"]/div[3]/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_selectStore(self):
        self.click(IndianMealKit.selectStore)

    def click_CurryBox(self):
        self.click(IndianMealKit.curryBox)

    def click_selectDate(self):
        self.click(IndianMealKit.selectDate)

    def click_Date(self):
        self.click(IndianMealKit.chooseDate)

    def click_ChangeSlot(self):
        element = self.driver.find_element_by_xpath(
            '//*[@id="dvDialog-Slot-DateTime"]/div/div/div[3]/a[1]')
        self.driver.execute_script("arguments[0].click();", element)