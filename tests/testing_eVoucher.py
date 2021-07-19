import time
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
        time.sleep(1)
        self.eVoucher_page.click_fresh()
        self.eVoucher_page.click_additem()
        self.eVoucher_page.click_AddItem1()
        self.eVoucher_page.click_MiniCart()
        self.eVoucher_page.click_Checkout()
        self.eVoucher_page.click_Checkout2()

    def test_checkInputMoreThanTextbox(self):
        self.eVoucher_page.EnterEvoucher("131618331813184844608426108494546449")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkInputLessThanTextbox(self):
        self.eVoucher_page.EnterEvoucher("13161833181318484460842610")
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

    def test_checkCopyPaste(self):
        self.eVoucher_page.EnterEvoucher1("12458")
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

    def test_checkInputLowerCaseAlphabets(self):
        self.eVoucher_page.EnterEvoucher("acvfdsbsdjv")
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

    def test_checkSpecialCharacters(self):
        self.eVoucher_page.EnterEvoucher("!@#$%^&*()_+|}{:?><';/.,`")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        self.assertEqual(self.actual2, Invalid)

    def test_checkAllowSpecialCharacters(self):
        self.eVoucher_page.EnterEvoucher("!@#$%^&*()_+|}{:?><';/.,`")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkHTMLCharacters(self):
        self.eVoucher_page.EnterEvoucher("<h1>My First Heading</h1>")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkJavaScriptHTMLCharacters(self):
        self.eVoucher_page.EnterEvoucher("var x = 5;")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkSQLInjectionCharacters(self):
        self.eVoucher_page.EnterEvoucher("SELECT * FROM Users WHERE UserId = 105 OR 1=1;")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkOnlySpaces(self):
        self.eVoucher_page.EnterEvoucher("        ")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkBlankInput(self):
        self.eVoucher_page.EnterEvoucher("")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkTrailingSpaces(self):
        self.eVoucher_page.EnterEvoucher("    15d6c")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)

    def test_checkLeadingSpaces(self):
        self.eVoucher_page.EnterEvoucher("15d6c     ")
        self.eVoucher_page.click_apply()
        Invalid = self.eVoucher_page.get_attribute(Coupon.InvalidCoupon, 'innerHTML')
        print(Invalid)
        print("field allows all special characters")
        self.assertEqual(self.actual2, Invalid)
