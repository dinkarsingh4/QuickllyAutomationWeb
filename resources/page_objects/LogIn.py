from resources.config_methods import DataClass
from resources.locators import LogIn
from resources.page_objects.base_page import BasePage


class Login(BasePage):
    """Privacy Error Page of Invisily Admin Portal"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def click_SignIn(self):
        self.click(LogIn.SignIn_button)

    def enter_email(self, email):
        self.find_elements(LogIn.email_textbox).clear()
        self.find_element(LogIn.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.find_elements(LogIn.password_textbox).clear()
        self.find_element(LogIn.password_textbox).send_keys(password)

    def click_login(self):
        # self.find_element_by_id(MainPage.login_button).click()
        print('Login Successful')
        self.click(LogIn.login_button)


    #def click_ForgetPassword(self):
        #self.click(LogIn.ForgetPassword_button)


