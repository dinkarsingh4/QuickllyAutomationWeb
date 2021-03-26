#!/usr/bin/env python3
from resources import ui_test_class
# from resources import
from resources.page_objects.LogIn import LogIn


class TesLogin(ui_test_class.UIClass):
    heading = 'quicklly'

    expected_res = "Email Address"
    expected_res1 = "Password"
    expected_res19 = "Log In"
    mp = {}

    @classmethod
    def setUpClass(cls):
        super(TesLogin, cls).setUpClass()

        # cls.driver.get(cls.base_page.base_url)

    @classmethod
    def tearDownClass(cls):
        super(TesLogin, cls).tearDownClass()
        # cls.driver.close()ii
        cls.driver.quit()

    def compare_res3(self):
        heading_login = self.maine_page.get_attribute(LogIn.login_heading, 'innerHTML')
        email_placeholder = self.maine_page.get_attribute(LogIn.email, 'placeholder')
        password_placeholder = self.maine_page.get_attribute(LogIn.pasw, 'placeholder')

        if self.expected_res19 == heading_login:
            self.mp = {'login': True}
            for pair in self.mp.items():
                print(pair)

        else:
            self.mp = {'login': False}
            for pair in self.mp.items():
                print(pair)



        if self.expected_res == email_placeholder:
            self.mp = {'email': True}
            for pair in self.mp.items():
                print(pair)


        else:
            self.mp = {'email': False}
            for pair in self.mp.items():
                print(pair)


        # pass

        if self.expected_res1 == password_placeholder:
            self.mp = {'password': True}
            for pair in self.mp.items():
                print(pair)

        else:
            self.mp = {'password': False}
            for pair in self.mp.items():
                print(pair)

        self.assertTrue(all(self.mp.values()), self.mp)




    def test_Login(self):
        """Login"""

        self.maine_page.click_SignIn()

        self.maine_page.enter_email("admin@gmail.com")
        self.maine_page.enter_password("admin1234")

        # time.sleep(55)
        self.maine_page.click_login()
        # print("placeholders are correct")
        # self.assertTrue(all(a.vakues()), a)


    def test_login_placeholders(self):

        self.compare_res3()


if __name__ == "__main__":
    import HtmlTestRunner, unittest

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports', report_title='Signup'))
