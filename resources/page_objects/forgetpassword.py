from resources.config_methods import DataClass
from resources.locators import ForgetPassword
from resources.page_objects.base_page import BasePage


class forgetpass(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_SIbutton(self):
        self.click(ForgetPassword.SI_button)

    def click_forgetpassword(self):
        self.click(ForgetPassword.ForgetPassword_button)

    def registred_email(self, remail):
        self.find_elements(ForgetPassword.registered_email).clear()
        self.find_element(ForgetPassword.registered_email).send_keys(remail)

    def click_submit(self):
        self.click(ForgetPassword.submit_button)

    def click_user_login(self):
        self.click(ForgetPassword.Uer_login)
