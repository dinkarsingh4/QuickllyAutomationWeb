from resources import ui_test_class
import HtmlTestRunner
import unittest
from resources.page_objects.needaccount import NeedAnAccount
from resources.page_objects.needaccount import needanaccount


class TesNAC(ui_test_class.UIIIClass):
    need_page: needanaccount
    need_page: NeedAnAccount
    expected_res8 = "First Name"
    expected_res9 = "Last Name"
    expected_res10 = "Enter your address"
    expected_res11 = "Apartment, Suite, Building (Optional)"
    expected_res12 = "Phone (ex:333-545-6789)"
    expected_res13 = "Email Address"
    expected_res14 = "Password"
    expected_res15 = "Confirm Password"
    expected_text_1 = "Register with us"
    expected_text_2 = "Register"
    dict1 = {}
    dicttxt = {}

    @classmethod
    def setUpClass(cls):
        super(TesNAC, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesNAC, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        super(TesNAC, self).setUp()
        self.base_page.driver.refresh()

    def compare_res_placeholders(self):

        firname_placeholder = self.need_page.get_attribute(NeedAnAccount.firname, 'placeholder')
        lasname_placeholder = self.need_page.get_attribute(NeedAnAccount.lasname, 'placeholder')
        add_placeholder = self.need_page.get_attribute(NeedAnAccount.enteraddress, 'placeholder')
        apart_placeholder = self.need_page.get_attribute(NeedAnAccount.apartmentno, 'placeholder')
        mobileno_placeholder = self.need_page.get_attribute(NeedAnAccount.mobileno, 'placeholder')
        emailadd_placeholder = self.need_page.get_attribute(NeedAnAccount.email2, 'placeholder')
        passw_placeholder = self.need_page.get_attribute(NeedAnAccount.pass2, 'placeholder')
        confirmpass_placeholder = self.need_page.get_attribute(NeedAnAccount.ConfirmPassword, 'placeholder')

        if self.expected_res8 == firname_placeholder:
            self.dict1['firstname'] = True

        else:
            self.dict1['firstname'] = False

        if self.expected_res9 == lasname_placeholder:
            self.dict1['lastname'] = True

        else:
            self.dict1['lastname'] = False

        if self.expected_res10 == add_placeholder:
            self.dict1['full address'] = True

        else:
            self.dict1['full address'] = False

        if self.expected_res11 == apart_placeholder:
            self.dict1['apartment'] = True

        else:
            self.dict1['apartment'] = False

        if self.expected_res12 == mobileno_placeholder:
            self.dict1['mobile number'] = True

        else:
            self.dict1['mobile number'] = False

        if self.expected_res13 == emailadd_placeholder:
            self.dict1['email'] = True

        else:
            self.dict1['email'] = False

        if self.expected_res14 == passw_placeholder:
            self.dict1['password'] = True

        else:
            self.dict1['password'] = False

        if self.expected_res15 == confirmpass_placeholder:
            self.dict1['confirm password'] = True
            print(self.dict1)

        else:
            self.dict1['confirm password'] = False
            print(self.dict1)

        self.assertTrue(all((self.dict1.values())), self.dict1)

    def compare_res_fieldsRequired(self):

        firstname_field = self.need_page.get_attribute(NeedAnAccount.firstname_error, 'innerHTML')
        add_field = self.need_page.get_attribute(NeedAnAccount.address_error, 'innerHTML')
        mobileno_field = self.need_page.get_attribute(NeedAnAccount.mobile_error, 'innerHTML')
        emailadd_field = self.need_page.get_attribute(NeedAnAccount.email_error, 'innerHTML')
        passw_field = self.need_page.get_attribute(NeedAnAccount.password_error, 'innerHTML')
        confirmpass_field = self.need_page.get_attribute(NeedAnAccount.confirm_password_error, 'innerHTML')
        print(firstname_field + ": firstname")
        print(add_field + ": address")
        print(mobileno_field + ": mobile number")
        print(emailadd_field + ": email")
        print(passw_field + ": pass")
        print(confirmpass_field + ": confirm password")

    def compare_res_getTexts(self):

        register_text = self.need_page.get_text(NeedAnAccount.registertext)
        submit_text = self.need_page.get_attribute(NeedAnAccount.register_button, 'value')

        if self.expected_text_1 == register_text:
            self.dicttxt['Register with us'] = True

        else:
            self.dicttxt['Register with us'] = False

        if self.expected_text_2 == submit_text:
            self.dicttxt['Register'] = True
            print(self.dicttxt)

        else:
            self.dicttxt['Register'] = False
            print(self.dicttxt)

    def test_NeedAnAccount(self):

        """Need An Account"""
        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        self.need_page.Firstname("Sami")
        self.need_page.Lastname("Adil")
        self.need_page.enter_address("Lahore, Pakistan")
        self.need_page.enter_apartment("")
        self.need_page.mobile("333-709-6671")
        self.need_page.enteremail("msamiadil@gmail.com")
        self.need_page.password("sami1234")
        self.need_page.confirm_password("sami1234")
        self.need_page.register_button()
        print("Registered Successfully")

    def test_placeholders(self):

        """Placeholders for NeedAnAccount Page"""
        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        self.compare_res_placeholders()

    def test_FieldsRequired(self):

        """Fields Required for NeedAnAccount Page"""
        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        self.need_page.register_button()
        self.compare_res_fieldsRequired()

    def test_Texts(self):

        """Headings for NeedAnAccount Page"""
        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        self.compare_res_getTexts()
        self.assertTrue(all(self.dicttxt.values()), self.dicttxt)

    def test_check_UserLogin(self):

        """NeedAnAccount Page"""
        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        userlogin_check = self.need_page.get_attribute(NeedAnAccount.userlogin_link, 'innerHTML')
        print(userlogin_check)

    def test_check_ContinueAsGuest(self):

        """NeedAnAccount Page"""
        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        CAG_check = self.need_page.get_attribute(NeedAnAccount.continue_as_guest_link, 'innerHTML')
        print(CAG_check)

    """Invalid Inputs for NeedAnAccount Page"""

    def test_check_invalidMob_input(self):

        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        self.need_page.mobile("1234")
        self.need_page.register_button()
        mob_invalid_check = self.need_page.get_attribute(NeedAnAccount.mobile_invalid, 'innerHTML')
        print(mob_invalid_check)

    def test_check_invalidEmail_input(self):

        self.need_page.click_sign_button()
        self.need_page.click_NeedAnAccount()
        self.need_page.enteremail("msamiadil")
        self.need_page.register_button()
        email_invalid_check = self.need_page.get_attribute(NeedAnAccount.email_invalid, 'innerHTML')
        print(email_invalid_check)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports', report_title='Signup - Need_an_Account'))
