from resources import ui_test_class
from resources.page_objects.needaccount import NeedAnAccount
from resources.page_objects.needaccount import needanaccount


# noinspection PyArgumentList
class TesNAC(ui_test_class.UIIIClass):
    need_page = needanaccount
    expected_res8 = "First Name"
    expected_res9 = "Last Nae"
    expected_res10 = "Enter your address"
    expected_res11 = "Apartment, Suite, Building (Optional)"
    expected_res12 = "Phone (ex:333-545-6789)"
    expected_res13 = "Email Address"
    expected_res14 = "Passwrd"
    expected_res15 = "Confirm Password"
    dict1 = {}

    @classmethod
    def setUpClass(cls):
        super(TesNAC, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesNAC, cls).tearDownClass()
        cls.driver.quit()

    def compare_res1(self):

        self.firname_placeholder = self.need_page.get_attribute(NeedAnAccount.firname, 'placeholder')
        self.lasname_placeholder = self.need_page.get_attribute(NeedAnAccount.lasname, 'placeholder')
        self.add_placeholder = self.need_page.get_attribute(NeedAnAccount.enteraddress, 'placeholder')
        self.apart_placeholder = self.need_page.get_attribute(NeedAnAccount.apartmentno, 'placeholder')
        self.mobileno_placeholder = self.need_page.get_attribute(NeedAnAccount.mobileno, 'placeholder')
        self.emailadd_placeholder = self.need_page.get_attribute(NeedAnAccount.email2, 'placeholder')
        self.passw_placeholder = self.need_page.get_attribute(NeedAnAccount.pass2, 'placeholder')
        self.confirmpass_placeholder = self.need_page.get_attribute(NeedAnAccount.ConfirmPassword, 'placeholder')

        if self.expected_res8 == self.firname_placeholder:
            self.dict1 = {'firstname': True}
            for pair in self.dict1.items():
                print(pair)
        else:
            self.dict1 = {'firstname': False}
            for pair in self.dict1.items():
                print(pair)
        pass

        if self.expected_res9 == self.lasname_placeholder:
            self.dict1 = {'lastname': True}
            for pair in self.dict1.items():
                print(pair)

        else:
            self.dict1 = {'lastname': False}
            for pair in self.dict1.items():
                print(pair)

        pass

        if self.expected_res10 == self.add_placeholder:
            self.dict1 = {'full address': True}
            for pair in self.dict1.items():
                print(pair)
        else:
            self.dict1 = {'full address': False}
            for pair in self.dict1.items():
                print(pair)

        if self.expected_res11 == self.apart_placeholder:
            self.dict1 = {'apartment': True}
            for pair in self.dict1.items():
                print(pair)
        else:
            self.dict1 = {'apartment': False}
            for pair in self.dict1.items():
                print(pair)

        if self.expected_res12 == self.mobileno_placeholder:
            self.dict1 = {'mobile number': True}
            for pair in self.dict1.items():
                print(pair)
        else:
            self.dict1 = {'mobile number': False}
            for pair in self.dict1.items():
                print(pair)

        if self.expected_res13 == self.emailadd_placeholder:
            self.dict1 = {'email': True}
            for pair in self.dict1.items():
                print(pair)
        else:
            self.dict1 = {'email': False}
            for pair in self.dict1.items():
                print(pair)

        if self.expected_res14 == self.passw_placeholder:
            self.dict1 = {'password': True}
            for pair in self.dict1.items():
                print(pair)
        else:
            self.dict1 = {'password': False}
            for pair in self.dict1.items():
                print(pair)

        if self.expected_res15 == self.confirmpass_placeholder:
            self.dict1 = {'Confirm password': True}
            for pair in self.dict1.items():
                print(pair)
        else:
            self.dict1 = {'Confirm password': False}
            for pair in self.dict1.items():
                print(pair)

        self.assertTrue(all((self.dict1.values())), self.dict1)

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

    def test_placeholders(self):

        """Placeholders for NeedAnAccount Page"""
        self.compare_res1()
        # self.assertTrue(all(self.dict1.values()), self.dict1)
