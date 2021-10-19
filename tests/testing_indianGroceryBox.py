import time
from resources import ui_test_class
from resources.page_objects.indiangrocerybox import IndianGrocery
from resources.page_objects.indiangrocerybox import IndianGroceryBox
from selenium.webdriver.support.color import Color


class TesINDIANGROCERY(ui_test_class.UVXVXIIClass):
    grocerybox_page: IndianGroceryBox
    grocerybox_page: IndianGrocery

    actual1 = "Organic Grocery Box Subscription"
    actual2 = " Organic Indian Grocery"
    actual3 = "Search for products..."
    actual4 = "Shipping"
    actual5 = "Minimum Order"
    actual6 = "Free"
    actual7 = "$0.00"
    actual8 = "What we Deliver"
    actual9 = "Authentic Indian Products"
    actual10 = "Unbeatable Prices"
    actual11 = "Customized Grocery Box"
    actual12 = "How it works"
    actual13 = "1. Build your organic grocery box"
    actual14 = "2. Select products"
    actual15 = "3. Set your frequency"
    actual16 = "Order Customized Organic Grocery Box"
    actual17 = "#f9660d"
    actual18 = "Organic Products"

    @classmethod
    def setUpClass(cls):
        super(TesINDIANGROCERY, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANGROCERY, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.grocerybox_page.zip("60611")
        self.grocerybox_page.submit_zip()
        search = self.grocerybox_page.get_attribute(IndianGroceryBox.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        for i in range(3):
            time.sleep(1)
            self.grocerybox_page.click_RightArrow()
        self.grocerybox_page.click_MealKit()
        self.grocerybox_page.click_indianGrocery()
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.indianGroceryLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_labelSubscription(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.subscription, 'innerHTML')
        print(label)
        self.assertEqual(self.actual1, label)

    def test_labelShipping(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.shipping, 'innerHTML')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelMinimum(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.minimum, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_labelFree(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.free, 'innerHTML')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelPrice(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.cost, 'innerHTML')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelWhatWeDeliver(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.whatwedeliver, 'innerHTML')
        print(label)
        self.assertEqual(self.actual8, label)

    def test_labelAuthentic(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.Authentic, 'innerHTML')
        print(label)
        self.assertEqual(self.actual9, label)

    def test_labelUnbeatable(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.Unbeatable, 'innerHTML')
        print(label)
        self.assertEqual(self.actual10, label)

    def test_labelCustomized(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.customized, 'innerHTML')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelHowItWorks(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.HowItWorks, 'innerHTML')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_labelBuild(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.build, 'innerHTML')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_labelSelectProducts(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.selectProducts, 'innerHTML')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_labelSelectFrequency(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.frequency, 'innerHTML')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_labelOrderCustomizedBox(self):
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.order, 'innerHTML')
        print(label)
        self.assertEqual(self.actual16, label)

    def test_clickweekly(self):
        self.grocerybox_page.click_weekly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.weekly.tablinks.active').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual17, hex)

    def test_clickbiweekly(self):
        self.grocerybox_page.click_Biweekly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.bi-weekly.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual17, hex)

    def test_clickmonthly(self):
        self.grocerybox_page.click_OIG()
        self.grocerybox_page.click_Monthly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.monthly.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual17, hex)

    def test_clickonce(self):
        self.grocerybox_page.click_Once()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.one-time.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual17, hex)

    def test_clickbuildABox(self):
        self.grocerybox_page.click_buildABox()
        label = self.grocerybox_page.get_attribute(IndianGroceryBox.organicProducts, 'innerHTML')
        print(label)
        self.assertEqual(self.actual18, label)
