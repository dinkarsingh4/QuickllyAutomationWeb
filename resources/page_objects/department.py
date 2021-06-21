from selenium.webdriver.remote.webelement import WebElement

from resources.config_methods import DataClass
from resources.locators import Department
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dept(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Department.enter_zip).clear()
        self.find_element(Department.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Department.submit_zip)

    def select_dropdown(self):
        self.click(Department.yourAccount)

    def click_signin(self):
        self.scroll_to_element(Department.SignInButton)
        self.click(Department.SignInButton)

    def EnterEmail(self, email):
        self.find_elements(Department.Email).clear()
        self.find_element(Department.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Department.Pass).clear()
        self.find_element(Department.Pass).send_keys(password)

    def click_login(self):
        self.click(Department.LoginButton)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(Department.proceed_to_checkOut)

    def click_payment1(self):
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_additem(self):
        self.scroll_to_element(Department.additem)
        element = self.driver.find_element_by_xpath('//*[@id="img_270"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(Department.Pay)

    def click_InstantPot(self):
        # WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(Department.Pot))
        # element = self.driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[1]/div/div/ul/li[8]/a')
        # self.driver.execute_script("arguments[0].click();", element)
        self.click(Department.Pot)

    def click_Department(self):
        self.click(Department.Department)

    def click_select(self):
        self.click(Department.select)

    def click_Add(self):
        self.scroll_to_element(Department.Add)
        self.click(Department.Add)

    def click_quicklly(self):
        self.click(Department.quicklly)
