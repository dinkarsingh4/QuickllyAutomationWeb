import time
from resources import ui_test_class
from resources.page_objects.guestlogin import LoginAsGuest
from resources.page_objects.guestlogin import GuestLogin


class TesGUESTLOGIN(ui_test_class.UVXVIClass):
    guestLogin_page: LoginAsGuest
    guestLogin_page: GuestLogin

    @classmethod
    def setUpClass(cls):
        super(TesGUESTLOGIN, cls).setUpClass()

    def food(self):
        self.guestLogin_page.submit_zip()
        time.sleep(2)
        self.guestLogin_page.click_food()
        time.sleep(2)
        self.guestLogin_page.click_MakkiFood()
        self.guestLogin_page.click_addTenders()
        self.guestLogin_page.click_AddToCartTenders()
        time.sleep(4)
        self.guestLogin_page.click_submitTenders()
        self.guestLogin_page.click_MiniCart()
        self.guestLogin_page.click_Checkout()
        # self.guestLogin_page.click_guestLogin()
        # self.guestLogin_page.Enter_Name("quicklly")
        # self.guestLogin_page.Enter_Name2("test")
        # self.guestLogin_page.EnterAddress("East Chicago Avenue, Chicago, IL 60611, USA")
        # self.guestLogin_page.EnterNumber("1452336548")
        # self.guestLogin_page.Enter_email("qicklly1234@gmail.com")
        # self.guestLogin_page.click_submit()
        self.guestLogin_page.click_payment1()
        time.sleep(10)
        # self.guestLogin_page.EnterCardNumber("5555444433331111")
        # time.sleep(5)
        # self.guestLogin_page.EnterExpirationDate("0225")
        # self.guestLogin_page.EnterCVV("158")
        # time.sleep(5)
        self.guestLogin_page.click_Pay()
        time.sleep(20)
        self.guestLogin_page.click_quicklly()
        # self.guestLogin_page.submit_zip()
        # time.sleep(25)

    def Catering(self):
        # self.guestLogin_page.submit_zip()
        time.sleep(2)
        self.guestLogin_page.click_LeftArrow()
        self.guestLogin_page.click_Catering()
        time.sleep(1)
        self.guestLogin_page.click_Hyderabad()
        time.sleep(2)
        self.guestLogin_page.click_AddBeef()
        self.guestLogin_page.click_AddToCartBeef()
        self.guestLogin_page.click_Delivery()
        time.sleep(5)
        self.guestLogin_page.click_timeOfDelivery()
        self.guestLogin_page.Submit_Beef()
        self.guestLogin_page.click_MiniCart()
        time.sleep(5)
        self.guestLogin_page.click_Checkout()
        self.guestLogin_page.click_guestLogin()
        self.guestLogin_page.Enter_Name("quicklly")
        self.guestLogin_page.Enter_Name2("test")
        self.guestLogin_page.EnterAddress("East Chicago Avenue, Chicago, IL 60611, USA")
        self.guestLogin_page.EnterNumber("1452336548")
        self.guestLogin_page.Enter_email("qicklly1234@gmail.com")
        self.guestLogin_page.click_submit()
        time.sleep(5)
        self.guestLogin_page.click_payment1()
        time.sleep(5)
        self.guestLogin_page.click_Pay()
        time.sleep(20)
        self.guestLogin_page.click_quicklly()

    def tiffin(self):
        # self.guestLogin_page.click_quicklly()
        self.guestLogin_page.submit_zip()
        time.sleep(2)
        self.guestLogin_page.click_Tiffin()
        time.sleep(1)
        self.guestLogin_page.click_Chicago()
        self.guestLogin_page.select_VegThali()
        self.guestLogin_page.click_AddToCartVT()
        # self.depart_page.submitVT()
        # self.depart_page.click_AddToCartVT()
        self.guestLogin_page.click_MiniCart()
        self.guestLogin_page.click_Checkout()
        self.guestLogin_page.click_payment1()
        time.sleep(5)
        self.guestLogin_page.click_Pay()
        time.sleep(20)
        self.guestLogin_page.click_quicklly()

    @classmethod
    def tearDownClass(cls):
        super(TesGUESTLOGIN, cls).tearDownClass()
        cls.driver.quit()

    def test_ZipCode(self):
        self.guestLogin_page.EnterZip("60611")
        self.guestLogin_page.submit_zip()

    def test_food(self):
        self.food()

    def test_catering(self):
        self.Catering()

    def test_tiffin(self):
        self.tiffin()
