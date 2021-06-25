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

    def InstantPot(self):
        # self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_fresh()
        self.depart_page.click_additem()
        # self.depart_page.click_additem()
        self.depart_page.click_Department()
        self.depart_page.click_InstantPot()
        self.depart_page.click_select()
        time.sleep(5)
        self.depart_page.click_Add()
        self.depart_page.click_AddToCart()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        self.depart_page.click_Pay()

    def food(self):
        time.sleep(2)
        self.depart_page.click_food()
        self.depart_page.click_MakkiFood()
        self.depart_page.click_addTenders()
        self.depart_page.click_AddToCartTenders()
        self.depart_page.click_submitTenders()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()

    def Grocery(self):
        time.sleep(1)
        self.depart_page.click_fresh()
        self.depart_page.click_additem()
        self.depart_page.click_ADDLG()
        self.depart_page.click_addPotato()
        self.depart_page.click_AddToCartPotato()
        self.depart_page.click_MiniCart1()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()

    def BBQKIT(self):
        time.sleep(1)
        self.depart_page.click_BBQ()
        self.depart_page.click_TikkaImage()
        self.depart_page.click_AddChickenTikkaToCart()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()

    def Catering(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_fresh()
        self.depart_page.click_additem()
        self.depart_page.click_Department()
        self.depart_page.click_Catering()
        self.depart_page.click_Hyderabad()
        self.depart_page.click_AddBeef()
        self.depart_page.click_AddToCartBeef()
        self.depart_page.click_Delivery()
        time.sleep(5)
        self.depart_page.click_timeOfDelivery()
        self.depart_page.Submit_Beef()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()

    def MealBasket(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_RightArrow()
        self.depart_page.click_mealBasket()
        self.depart_page.select_mealPlan()
        self.depart_page.click_Korma()
        for i in range(5):
            self.depart_page.Plus_Korma()
        self.depart_page.click_AddToCartCK()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        time.sleep(5)
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()

    def tiffin(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_Tiffin()
        self.depart_page.click_Chicago()
        self.depart_page.select_VegThali()
        self.depart_page.click_AddToCartVT()
        self.depart_page.submitVT()
        self.depart_page.click_AddToCartVT()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        time.sleep(5)
        self.depart_page.click_payment1()
        self.depart_page.click_Pay()

    def MealKit(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_MealKit()
        self.depart_page.click_CuminCLub()
        self.depart_page.select_MealPlan20()
        self.depart_page.click_Papad()
        for i in range(19):
            self.depart_page.Plus_Papad()
        self.depart_page.click_AddToCartPapad()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()

    def recipes(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(5)
        self.depart_page.click_fresh()
        self.depart_page.click_additem()
        self.depart_page.click_Department()
        self.depart_page.click_Recipes()
        self.depart_page.click_PalakPaneer()
        # time.sleep(5)
        self.depart_page.click_TickBox()
        self.depart_page.click_AddToBasket()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()

    def test_EnterZipCode(self):
        self.depart_page.zip("60611")
        self.depart_page.submit_zip()

    def test_SignIN(self):
        self.depart_page.select_dropdown()
        self.depart_page.click_signin()
        self.depart_page.EnterEmail("quicklly1234@gmail.com")
        self.depart_page.EnterPass("123456")
        self.depart_page.click_login()

    def test_shopWithGrocery(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        self.Grocery()

    def test_shopWithInstant(self):
        # self.depart_page.click_quicklly()
        self.InstantPot()

    def test_shopWithFood(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        self.food()

    def test_shopWithBBQ(self):
        self.BBQKIT()

    def test_shopWithCatering(self):
        self.Catering()

    def test_shopWithMealBasket(self):
        self.MealBasket()

    def test_shopWithTiffin(self):
        self.tiffin()

    def test_shopWithMealKit(self):
        self.MealKit()

    def test_shopWithTrecipes(self):
        self.recipes()



    # def test_z(self):
    #     self.depart_page.click_quicklly()
    #     self.depart_page.submit_zip()
    #     self.depart_page.click_MiniCart()
    #     self.depart_page.click_seeti()
    #     self.depart_page.click_remove()
