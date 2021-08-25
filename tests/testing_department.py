import time
from resources import ui_test_class
from resources.page_objects.department import Department
from resources.page_objects.department import Dept


class TesDEPARTMENT(ui_test_class.UVIIClass):
    depart_page: Dept
    depart_page: Department

    actual1 = "Thank you"
    actual2 = "Your account"
    actual3 = "Search for products..."

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def InstantPot(self):
        self.depart_page.submit_zip()
        time.sleep(2)
        for i in range(3):
            self.depart_page.click_LeftArrow()
            time.sleep(1)
        self.depart_page.click_InstantPot()
        self.depart_page.click_select()
        time.sleep(5)
        self.depart_page.click_Add()
        self.depart_page.click_AddToCart()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        # self.depart_page.click_payment1()
        # self.depart_page.click_Pay()

    def food(self):
        time.sleep(2)
        self.depart_page.click_food()
        time.sleep(2)
        self.depart_page.click_MakkiFood()
        self.depart_page.click_addTenders()
        self.depart_page.click_AddToCartTenders()
        time.sleep(4)
        self.depart_page.click_submitTenders()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

    def Grocery(self):
        time.sleep(1)
        self.depart_page.click_fresh()
        self.depart_page.click_additem()
        self.depart_page.click_ADDLG()
        time.sleep(5)
        self.depart_page.click_addPotato()
        self.depart_page.click_AddToCartPotato()
        self.depart_page.click_MiniCart1()
        self.depart_page.click_Checkout()
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

    def BBQKIT(self):
        time.sleep(5)
        self.depart_page.click_BBQ()
        self.depart_page.click_TikkaImage()
        self.depart_page.click_AddChickenTikkaToCart()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_Checkout2()
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

    def Catering(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_LeftArrow()
        self.depart_page.click_Catering()
        time.sleep(1)
        self.depart_page.click_Hyderabad()
        self.depart_page.click_AddBeef()
        self.depart_page.click_AddToCartBeef()
        self.depart_page.click_Delivery()
        time.sleep(5)
        self.depart_page.click_timeOfDelivery()
        self.depart_page.Submit_Beef()
        self.depart_page.click_MiniCart()
        time.sleep(5)
        self.depart_page.click_Checkout()
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

    def MealBasket(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        for i in range(2):
            self.depart_page.click_RightArrow()
            time.sleep(1)
        time.sleep(2)
        self.depart_page.click_mealBasket()
        self.depart_page.select_mealPlan()
        self.depart_page.click_Korma()
        for i in range(5):
            self.depart_page.Plus_Korma()
        self.depart_page.click_AddToCartCK()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        time.sleep(5)
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

    def tiffin(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_Tiffin()
        self.depart_page.click_Chicago()
        self.depart_page.select_VegThali()
        self.depart_page.click_AddToCartVT()
        self.depart_page.submitVT()
        # self.depart_page.click_AddToCartVT()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        # time.sleep(5)
        # self.depart_page.click_payment1()
        # self.depart_page.click_Pay()

    def MealKit(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_RightArrow()
        time.sleep(10)
        self.depart_page.click_MealKit()
        self.depart_page.click_CuminCLub()
        self.depart_page.select_MealPlan20()
        self.depart_page.click_Papad()
        for i in range(19):
            self.depart_page.Plus_Papad()
        self.depart_page.click_AddToCartPapad()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

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
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

    def OrganicGrocery(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(10)
        self.depart_page.click_OrganicGrocery()
        self.depart_page.click_BuildBox()
        self.depart_page.click_AddJowar()
        self.depart_page.click_AddToCartJowar()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        # self.depart_page.click_payment1()
        # time.sleep(5)
        # self.depart_page.click_Pay()

    def Rotikaa(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_rotiKit()
        self.depart_page.click_RotiBox()
        self.depart_page.click_AddWholeWheatRoti()
        self.depart_page.click_AddToCartRoti()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()

    def Liquor(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        time.sleep(2)
        self.depart_page.click_Liquor()
        # self.depart_page.click_beer()
        self.depart_page.click_classicLime()
        self.depart_page.click_AddToCartBeer()
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()

    def test_EnterZipCode(self):
        self.depart_page.zip("60611")
        self.depart_page.submit_zip()
        search = self.depart_page.get_attribute(Department.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIN(self):
        self.depart_page.select_dropdown()
        self.depart_page.click_signin()
        self.depart_page.EnterEmail("testaccount@quicklly.com")
        self.depart_page.EnterPass("123456")
        self.depart_page.click_login()
        AccountLabel = self.depart_page.get_attribute(Department.Account, 'innerHTML')
        print(AccountLabel)
        self.assertEqual(self.actual2, AccountLabel)

    def test_shopWithGrocery(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        self.Grocery()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithInstant(self):
        self.depart_page.click_quicklly()
        self.InstantPot()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithFood(self):
        self.depart_page.click_quicklly()
        self.depart_page.submit_zip()
        self.food()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithBBQ(self):
        self.BBQKIT()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithCatering(self):
        self.Catering()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithMealBasket(self):
        self.MealBasket()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithTiffin(self):
        self.tiffin()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithMealKit(self):
        self.MealKit()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithTrecipes(self):
        self.recipes()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithOrganicGrocery(self):
        self.OrganicGrocery()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithRotikaa(self):
        self.Rotikaa()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)

    def test_shopWithLiquor(self):
        self.Liquor()
        # ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        # print(ThankYouLabel)
        # self.assertEqual(self.actual1, ThankYouLabel)
