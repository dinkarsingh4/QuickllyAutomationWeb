import time
from resources import ui_test_class
from resources.page_objects.chaiDepartment import ChaiAndCoffee
from resources.page_objects.chaiDepartment import CACD
from selenium.webdriver.support.color import Color


class TesCHAIDEPARTMENT(ui_test_class.UVXVIXClass):
    chai_page: CACD
    chai_page: ChaiAndCoffee

    actual1 = "Chai Tea & Coffee Kit"
    actual2 = "Weekly"
    actual3 = "Search for products..."
    actual4 = "#333333"
    actual5 = " Indian Chai & Coffee"
    actual6 = "Kimbala Chai & Coffee Subscription"
    actual7 = "Our Collection"
    actual8 = "Chai Assamica"
    actual9 = "Chai Concentrate"
    actual10 = "Coffee a la Jaggery"
    actual11 = "Coffee Neat"
    actual12 = "Dirty Chai Concentrate"
    actual13 = "Ready-to-Drink Chai"
    actual14 = "Ready-to-Drink Coffee"
    actual15 = "About Kimbala"
    actual16 = "Thank you"

    @classmethod
    def setUpClass(cls):
        super(TesCHAIDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCHAIDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def BactToPage(self):
        self.chai_page.click_quicklly()
        self.chai_page.zip("60611")
        self.chai_page.submit_zip()
        time.sleep(2)
        for i in range(11):
            time.sleep(1)
            self.chai_page.click_RightArrow()
        self.chai_page.click_ChaiAndCoffee()

    def Payment(self):
        self.chai_page.click_buildABox()
        self.chai_page.click_AddKimbala()
        self.chai_page.click_MiniCart()
        self.chai_page.click_Checkout()
        self.chai_page.click_Checkout2()
        self.chai_page.click_payment1()
        time.sleep(5)
        self.chai_page.click_Pay()

    def Signin(self):
        self.chai_page.select_dropdown()
        self.chai_page.click_signin()
        self.chai_page.EnterEmail("testaccount@quicklly.com")
        self.chai_page.EnterPass("123456")
        self.chai_page.click_login()

    def test_EnterZipCode(self):
        self.chai_page.zip("60611")
        self.chai_page.submit_zip()
        self.Signin()
        search = self.chai_page.get_attribute(ChaiAndCoffee.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickChaiDepartment(self):
        time.sleep(2)
        for i in range(11):
            time.sleep(1)
            self.chai_page.click_RightArrow()
        self.chai_page.click_ChaiAndCoffee()
        headingLabel = self.chai_page.get_attribute(ChaiAndCoffee.heading1, 'textContent')
        print(headingLabel)
        self.assertEqual(self.actual1, headingLabel)

    def test_weekly(self):
        self.chai_page.click_weekly()
        self.Payment()
        thankYou = self.chai_page.get_attribute(ChaiAndCoffee.ThankYou, 'innerHTML')
        print(thankYou)
        self.assertEqual(self.actual16, thankYou)

    def test_monthly(self):
        self.chai_page.click_Monthly()
        self.Payment()
        thankYou = self.chai_page.get_attribute(ChaiAndCoffee.ThankYou, 'innerHTML')
        print(thankYou)
        self.assertEqual(self.actual16, thankYou)

    def test_once(self):
        self.BactToPage()
        self.chai_page.click_once()
        self.Payment()
        thankYou = self.chai_page.get_attribute(ChaiAndCoffee.ThankYou, 'innerHTML')
        print(thankYou)
        self.assertEqual(self.actual16, thankYou)

    def test_clickbuildABox(self):
        self.chai_page.click_buildABox()
        indianLabel = self.chai_page.get_attribute(ChaiAndCoffee.indianChaiLabel, 'textContent')
        print(indianLabel)
        self.assertEqual(self.actual5, indianLabel)

    def test_subscriptionLabel(self):
        Slabel = self.chai_page.get_attribute(ChaiAndCoffee.subscription, 'textContent')
        print(Slabel)
        self.assertEqual(self.actual6, Slabel)

    def test_ourCollection(self):
        self.BactToPage()
        Label = self.chai_page.get_attribute(ChaiAndCoffee.collection, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual7, Label)

    def test_labelchaiAssamica(self):
        Label = self.chai_page.get_attribute(ChaiAndCoffee.ChaiAssamica, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual8, Label)

    def test_coffeeJaggery(self):
        self.chai_page.click_backToPage()
        Label = self.chai_page.get_attribute(ChaiAndCoffee.CoffeeJaggery, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual9, Label)

    def test_coffeeNeat(self):
        Label = self.chai_page.get_attribute(ChaiAndCoffee.coffeeNeat, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual10, Label)

    def test_labelchaiConcentrate(self):
        Label = self.chai_page.get_attribute(ChaiAndCoffee.ChaiConcentrate, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual11, Label)

    def test_dirtyChai(self):
        Label = self.chai_page.get_attribute(ChaiAndCoffee.DirtyChai, 'innerHTML')
        print(Label)
        self.assertEqual(self.actual12, Label)

    def test_readyToDrinkChai(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.readyChai, 'textContent')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_readyToDrinkCoffee(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.readyCoffee, 'textContent')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_kimbala(self):
        label = self.chai_page.get_attribute(ChaiAndCoffee.aboutKimbala, 'textContent')
        print(label)
        self.assertEqual(self.actual15, label)
