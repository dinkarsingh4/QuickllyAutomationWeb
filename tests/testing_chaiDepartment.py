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
    actual9 = "Coffee a la Jaggery"
    actual10 = "Coffee Neat"
    actual11 = "Chai Concentrate"
    actual12 = "Dirty Chai Concentrate"
    actual13 = "Ready-to-Drink Chai"
    actual14 = "Ready-to-Drink Coffee"
    actual15 = "About Kimbala"

    @classmethod
    def setUpClass(cls):
        super(TesCHAIDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCHAIDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.chai_page.zip("60611")
        self.chai_page.submit_zip()
        search = self.chai_page.get_attribute(ChaiAndCoffee.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickChaiDepartment(self):
        time.sleep(2)
        self.chai_page.click_ChaiAndCoffee()
        headingLabel = self.chai_page.get_attribute(ChaiAndCoffee.heading1, 'textContent')
        print(headingLabel)
        self.assertEqual(self.actual1, headingLabel)

    def test_weekly(self):
        self.chai_page.click_weekly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.weekly.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual4, hex)

    # def test_clickbiweekly(self):
    #     self.chai_page.click_BiWeekly()
    #     colorLabel = self.driver.find_element_by_css_selector(
    #         '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.bi-weekly.tablinks').value_of_css_property(
    #         'background-color')
    #     hex = Color.from_string(colorLabel).hex
    #     print(hex)
    #     self.assertEqual(self.actual4, hex)

    def test_monthly(self):
        self.chai_page.click_Monthly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.monthly.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual4, hex)

    def test_once(self):
        self.chai_page.click_once()
        onceColorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.one-time.tablinks.active').value_of_css_property(
            'background-color')
        hex = Color.from_string(onceColorLabel).hex
        print(hex)
        self.assertEqual(self.actual4, hex)

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
