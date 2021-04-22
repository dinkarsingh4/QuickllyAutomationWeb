from resources import ui_test_class
import unittest
from resources.page_objects.LogIn import LogIn


class TesLogin(ui_test_class.UIClass):
    heading = 'quicklly'

    expected_res = "Email Address"
    expected_res1 = "Password"
    expected_res19 = "Log In"
    expected_res20 = "Email :"
    expected_res21 = "Password :"
    mp = {}
    mp1 = {}

    @classmethod
    def setUpClass(cls):
        super(TesLogin, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesLogin, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        super(TesLogin, self).setUp()
        self.base_page.driver.refresh()

    def compare_placeholders(self):

        email_placeholder = self.maine_page.get_attribute(LogIn.email, 'placeholder')
        password_placeholder = self.maine_page.get_attribute(LogIn.pasw, 'placeholder')

        if self.expected_res == email_placeholder:
            self.mp['email'] = True

        else:
            self.mp['email'] = False

        if self.expected_res1 == password_placeholder:
            self.mp['password'] = True
            print(self.mp)

        else:
            self.mp['password'] = False
            print(self.mp)

        self.assertTrue(all(self.mp.values()), self.mp)

    def compare_res_texts(self):

        heading_login = self.maine_page.get_attribute(LogIn.login_heading, 'innerHTML')
        emailtext_heading = self.maine_page.get_attribute(LogIn.email_text, 'innerHTML')
        passwordtext_heading = self.maine_page.get_attribute(LogIn.password_text, 'innerHTML')

        if self.expected_res19 == heading_login:
            self.mp1['login'] = True

        else:
            self.mp1['login'] = False

        if self.expected_res20 == emailtext_heading:
            self.mp1['email'] = False

        else:
            self.mp1['email'] = False

        if self.expected_res21 == passwordtext_heading:
            self.mp1['password'] = True
            print(self.mp1)

        else:
            self.mp1['password'] = False
            print(self.mp1)

        self.assertTrue(all(self.mp1.values()), self.mp1)

    def compare_res_fields_required(self):

        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        password_field = self.maine_page.get_attribute(LogIn.password_field_error, 'innerHTML')
        print(email_field + ": Email")
        print(password_field + ": Password")

    def test_Login(self):

        """Login"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        self.base_page.capture_screen_shot()

    def test_login_placeholders(self):

        """placeholders for Login page"""
        self.maine_page.click_SignIn()
        self.compare_placeholders()

    def test_login_texts(self):

        """headings for Login page"""
        self.maine_page.click_SignIn()
        self.compare_res_texts()

    def test_FieldsRequired(self):

        """Fields Required for Login Page"""
        self.maine_page.click_SignIn()
        self.maine_page.click_login()
        self.compare_res_fields_required()

    def test_checkNeedAnAccount_link(self):

        """Login Page"""
        self.maine_page.click_SignIn()
        NeedAnAccount_check = self.maine_page.get_attribute(LogIn.needanaccount_signin, 'innerHTML')
        print(NeedAnAccount_check)

    def test_checkContinueAsGuest_link(self):

        """Login Page"""
        self.maine_page.click_SignIn()
        ContinueAsGuest_check = self.maine_page.get_attribute(LogIn.ContinueAsGuest_link, 'innerHTML')
        print(ContinueAsGuest_check)

    def test_forgotPassword_link(self):

        """Login Page"""
        self.maine_page.click_SignIn()
        ForgotPassword_check = self.maine_page.get_attribute(LogIn.ForgotPassword_link, 'innerHTML')
        print(ForgotPassword_check)

    def test_privacy_link(self):

        """Login Page"""
        self.maine_page.click_SignIn()
        self.maine_page.click_Privacy()
        print("Privacy link is clickable")

    def test_TermsAndConditions_link(self):

        """Login Page"""
        self.maine_page.click_SignIn()
        self.maine_page.click_TermsAndConditions()
        self.maine_page.click_home()
        print("Terms&Condition link is clickable")

    def test_DotBetweenEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin.123@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        print("Accepted")

    def test_DotBetweenSubDomain(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        print("Accepted")

    def test_DigitsInEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("123@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        print("Accepted")

    def test_UnderScoreInEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("123_abc@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        print("Accepted")

    def test_DashInEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("123-abc@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        print("Accepted")

    def test_ValidEmail(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("1123abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        print("Not Accepted")

    def test_ValidEmail2(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("@abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        print("Not Accepted")

    def test_ValidEmail3(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("abc@abc@abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        print("Not Accepted")

    def test_ValidEmail4(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("abc….....abc@abc.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        print("Not Accepted")

    def test_ValidEmail5(self):

        """Login Page Email Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("255.255. 255.255")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        email_field = self.maine_page.get_attribute(LogIn.email_field_error, 'innerHTML')
        print(email_field)
        print("Not Accepted")

    def test_EmailAndPassDontMatch(self):

        """Login Page Email&Password Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("admin1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)

    def test_password_minLength(self):

        """Login Page Password Validation"""
        self.maine_page.click_SignIn()
        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("1234")
        self.maine_page.click_login()
        error_messages = self.maine_page.get_attribute(LogIn.doesnt_match, 'innerHTML')
        print(error_messages)
