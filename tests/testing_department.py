import time
from resources import ui_test_class
from resources.page_objects.department import Department
from resources.page_objects.department import Dept


class TesDEPARTMENT(ui_test_class.UVIIClass):
    depart_page: Dept
    depart_page: Department

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.depart_page.zip("60611")
        self.depart_page.submit_zip()

    def test_SignIN(self):
        self.depart_page.select_dropdown()
        self.depart_page.click_signin()
        self.depart_page.EnterEmail("testaccount@quicklly.com")
        self.depart_page.EnterPass("123456")
        self.depart_page.click_login()

    # def test_shopByGrocery(self):
    #     self.depart_page.click_additem()
    #     self.depart_page.click_MiniCart()
    #     self.depart_page.click_Checkout()
    #     self.depart_page.click_payment1()
    #     self.depart_page.click_Pay()

    def test_shopWithMeal(self):
        # self.depart_page.click_quicklly()
        # self.depart_page.submit_zip()
        time.sleep(1)
        self.depart_page.click_additem()
        # self.depart_page.click_MiniCart()
        # self.depart_page.click_Checkout()
        self.depart_page.click_Department()
        self.depart_page.click_InstantPot()
        self.depart_page.click_select()
        self.depart_page.click_Add()

        self.depart_page.click_Pay()
