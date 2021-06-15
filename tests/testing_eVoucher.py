# import time
from resources import ui_test_class
from resources.locators import Coupon
from resources.page_objects.eVoucher import evoucher


class TesEVoucher(ui_test_class.UVIClass):
    eVoucher_page: evoucher
    eVoucher_page: Coupon

    actual1 = "Your cart is empty"
    actual2 = "Invalid Coupon.!"


    @classmethod
    def setUpClass(cls):
        super(TesEVoucher, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesEVoucher, cls).tearDownClass()
        cls.driver.quit()

    # def setUp(self):
    #     super(TesEVoucher, self).setUp()
    #     self.base_page.driver.refresh()

    def test_EnterZipcode(self):
        self.eVoucher_page.EnterZipcode("60611")
        self.eVoucher_page.ClickSubmit()
        empty = self.eVoucher_page.get_attribute(Coupon.empty_cart, 'innerHTML')
        print(empty)
        self.assertEqual(self.actual1, empty)

    def test_SignIn(self):
        self.eVoucher_page.select_dropdown()
        self.eVoucher_page.click_signin()
        self.eVoucher_page.EnterEmail("testaccount@quicklly.com")
        self.eVoucher_page.EnterPass("123456")
        self.eVoucher_page.click_login()

    def test_addItem(self):
        self.eVoucher_page.click_additem()
        self.eVoucher_page.click_AddItem1()
        self.eVoucher_page.click_MiniCart()
        self.eVoucher_page.click_Checkout()

    def test_checkInputMoreThanTextbox(self):
        self.eVoucher_page.EnterEvoucher("131618331813184844608426108494546449")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputNumbersOnly(self):
        self.eVoucher_page.EnterEvoucher("12458")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputDecimalNumbers(self):
        self.eVoucher_page.EnterEvoucher("52.4785")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputFormattedNumbers(self):
        self.eVoucher_page.EnterEvoucher("$110,00")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputAlphabets(self):
        self.eVoucher_page.EnterEvoucher("acvfdsbhjk")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputUpperCaseAlphabets(self):
        self.eVoucher_page.EnterEvoucher("ABXJUDBJNCU")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputMixAlphabets(self):
        self.eVoucher_page.EnterEvoucher("ABfgXJUer")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)
