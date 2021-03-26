from resources import ui_test_class
# import HTMLTestRunner
# import unittest
from resources.page_objects.guest import ContinueAsGuest
from resources.page_objects.guest import guest



class TesCAG(ui_test_class.UIIClass):
    guest_page: guest
    guest_page: ContinueAsGuest
    expected_res2 = "First Name"
    expected_res3 = "Last Name"
    expected_res4 = "Enter your address"
    expected_res5 = "Apartment, Suite, Building (Optional)"
    expected_res6 = "Phone (ex:333-545-6789)"
    expected_res7 = "Email Address"

    dict = {}

    @classmethod
    def setUpClass(cls):
        super(TesCAG, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCAG, cls).tearDownClass()
        # cls.driver.close()
        cls.driver.quit()

    def compare_res(self):

        firstname_placeholder = self.guest_page.get_attribute(ContinueAsGuest.firstname, 'placeholder')
        self.lastname_placeholder = self.guest_page.get_attribute(ContinueAsGuest.lastname, 'placeholder')
        self.address_placeholder = self.guest_page.get_attribute(ContinueAsGuest.fullAddress, 'placeholder')
        self.apartment_placeholder = self.guest_page.get_attribute(ContinueAsGuest.Apartment, 'placeholder')
        self.mob_placeholder = self.guest_page.get_attribute(ContinueAsGuest.MobileNumber, 'placeholder')
        self.mail_placeholder = self.guest_page.get_attribute(ContinueAsGuest.EmailAddress, 'placeholder')

        if self.expected_res2 == firstname_placeholder:
            self.dict['firstname'] = True

        else:
            self.dict['firstname'] = False

        if self.expected_res3 == self.lastname_placeholder:
            self.dict['lastname'] = True


        else:
            self.dict['lastname'] = False

        # pass

        if self.expected_res4 == self.address_placeholder:
            self.dict['full address'] = True

        else:
            self.dict['full address'] = False

        if self.expected_res5 == self.apartment_placeholder:
            self.dict['Apartment'] = True

        else:
            self.dict['Apartment'] = False


        if self.expected_res6 == self.mob_placeholder:
            self.dict['mobile number'] = True

        else:
            self.dict['mobile number'] = False

        if self.expected_res7 == self.mail_placeholder:
            self.dict['email'] = True
            print(self.dict)

        else:
            self.dict['email'] = False
            print(self.dict)

        self.assertTrue(all(self.dict.values()), self.dict)

    def test_ContinueAsGuest(self):

        """ContinueAsGuest"""

        self.guest_page.signin_button()
        self.guest_page.click_Continue_As_Guest()
        self.guest_page.first_name("saad")
        self.guest_page.last_name("Adil")
        self.guest_page.full_address("Lahore, Pakistan")
        self.guest_page.apartment("")
        self.guest_page.mobile_number("333-416-3429")
        self.guest_page.email_address('saadadil3@gmail.com')
        self.guest_page.click_submit()

    def test_placeholders(self):

        """Placeholders for ContinueAsGuest Page"""
        self.compare_res()
        # self.assertTrue(all(self.dict.values()), self.dict)


if __name__ == "__main__":

    import HtmlTestRunner, unittest

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports', report_title='Signup'))
