import time
from resources import ui_test_class
from resources.page_objects.monthly_page import Monthly
from resources.page_objects.monthly_page import MONTHLY


class TesMONTHLYORDER(ui_test_class.UVXVXVVClass):
    monthly_page: Monthly
    monthly_page: MONTHLY

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    actual4 = "5"

    @classmethod
    def setUpClass(cls):
        super(TesMONTHLYORDER, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesMONTHLYORDER, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.monthly_page.zip("60611")
        self.monthly_page.submit_zip()
        search = self.monthly_page.get_attribute(Monthly.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.monthly_page.select_dropdown()
        self.monthly_page.click_signin()
        self.monthly_page.EnterEmail("testaccount@quicklly.com")
        self.monthly_page.EnterPass("123456")
        self.monthly_page.click_login()
        self.monthly_page.select_dropdown()
        logoutLabel = self.monthly_page.get_attribute(Monthly.logout, 'innerHTML')
        print(logoutLabel)
        self.assertEqual(self.actual2, logoutLabel)

    def test_biWeeklyOrder(self):
        time.sleep(2)
        self.monthly_page.click_NationWideShop()
        self.monthly_page.click_indianSweet()
        self.monthly_page.click_monthly()
        self.monthly_page.click_buildABox()
        self.monthly_page.click_addMasalaMathai()
        for i in range(4):
            self.monthly_page.click_plusMasalaMathai()
        quantityLabel = self.monthly_page.get_attribute(Monthly.quantity, 'innerHTML')
        print(quantityLabel)
        self.assertEqual(self.actual4, quantityLabel)

    def test_biWeeklyOrderCheckout(self):
        self.monthly_page.click_addToCartMasala()
        time.sleep(2)
        self.monthly_page.click_Cart()
        self.monthly_page.click_Checkout()
        self.monthly_page.click_Checkout2()
        self.monthly_page.click_payment1()
        time.sleep(5)
        self.monthly_page.click_Pay()
        ThankYouLabel = self.monthly_page.get_attribute(Monthly.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)
