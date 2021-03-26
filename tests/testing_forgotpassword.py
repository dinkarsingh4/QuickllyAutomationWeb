from resources import ui_test_class
from resources.page_objects.forgetpassword import ForgetPassword
from resources.page_objects.forgetpassword import forgetpass


class TesFP(ui_test_class.UIIIIClass):
    expected_res16 = "Enter your registed Email Id"
    expected_res17 = "Forgot Password"
    expected_res18 = "Why register with us."
    fp = {}

    @classmethod
    def setUpClass(cls):
        super(TesFP, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesFP, cls).tearDownClass()
        cls.driver.quit()

    def compare_result2(self):

        forgotpassword_heading = self.forget_page.get_attribute(ForgetPassword.heading1, 'innerHTML')
        whyregister_heading = self.forget_page.get_attribute(ForgetPassword.heading2, 'innerHTML')
        registeredemail_placeholder = self.forget_page.get_attribute(ForgetPassword.registered_email, 'placeholder')

        if self.expected_res17 == forgotpassword_heading:
            self.fp['forgot password'] = True
            print(self.fp)


        else:
            self.fp['forgot password'] = False
            print(self.fp)

        if self.expected_res18 == whyregister_heading:
            self.fp['why register with us.'] = True
            print(self.fp)


        else:
            self.fp['why register with us.'] = False
            print(self.fp)

        self.assertTrue(all(self.fp.values()), self.fp)

        # pass
        #
        # if self.expected_res4 == self.address_placeholder:
        #     self.dict = {'full address': True}
        #     for pair in self.dict.items():
        #         print(pair)
        #
        # else:
        #     self.dict = {'full address': False}
        #     for pair in self.dict.items():
        #         print(pair)



    def test_ForgetPassword(self):
        """Forget Password"""

        self.forget_page.click_SIbutton()
        self.forget_page.click_forgetpassword()
        self.forget_page.registred_email("saadadil3@gmail.com")
        self.forget_page.click_submit()
        # print("placeholders are correct")
        # print("Headings are correct")

    def test_headings(self):
        self.compare_result2()



if __name__ == "__main__":
    import HtmlTestRunner, unittest

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports', report_title='Signup'))
