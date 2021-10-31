import time
from resources import ui_test_class
from resources.page_objects.rotikit import RotiBox
from resources.page_objects.rotikit import RotiKit
from selenium.webdriver.support.color import Color


class TesROTIKIT(ui_test_class.UVXVXIIIClass):
    roti_page: RotiKit
    roti_page: RotiBox

    actual1 = "Our Roti Categories"
    actual2 = " Order Roti Kit"
    actual3 = "Search for products..."
    actual4 = "Whole Wheat Roti"
    actual5 = "Fresh Tawa Roti"
    actual6 = "Roti"
    actual7 = "Multigrain Roti"
    actual8 = "Rotla"
    actual9 = "Paratha"
    actual10 = "Thepla"
    actual11 = "Specialty Roti"
    actual12 = "Bhakhri"
    actual13 = "Gluten Free"
    actual14 = "What We Deliver"
    actual15 = "Fresh Homemade Taste!"
    actual16 = "Premium Ingredients"
    actual17 = "Free Delivery"
    actual18 = "What are Rotis?"
    actual19 = "#446084"
    actual20 = "Free Delivery on Minimum Order"
    actual21 = "Indian Bread Roti Kit"

    @classmethod
    def setUpClass(cls):
        super(TesROTIKIT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesROTIKIT, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.roti_page.zip("60611")
        self.roti_page.submit_zip()
        search = self.roti_page.get_attribute(RotiKit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        for i in range(3):
            time.sleep(1)
            self.roti_page.click_RightArrow()
        self.roti_page.click_MealKit()
        self.roti_page.click_rotiKit()
        label = self.roti_page.get_attribute(RotiKit.RotiLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_labelCategories(self):
        label = self.roti_page.get_attribute(RotiKit.categories, 'innerHTML')
        print(label)
        self.assertEqual(self.actual1, label)

    def test_labelWholeWheat(self):
        label = self.roti_page.get_attribute(RotiKit.wholewheatlabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelRoti(self):
        label = self.roti_page.get_attribute(RotiKit.rotiLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelMultiGrain(self):
        label = self.roti_page.get_attribute(RotiKit.MultiGrainLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelRotla(self):
        label = self.roti_page.get_attribute(RotiKit.RotlaLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual8, label)

    def test_labelParatha(self):
        label = self.roti_page.get_attribute(RotiKit.ParathaLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual9, label)

    # def test_labelThepla(self):
    #     label = self.roti_page.get_attribute(RotiKit.TheplaLabel, 'innerHTML')
    #     print(label)
    #     self.assertEqual(self.actual10, label)

    def test_labelSpecialRoti(self):
        label = self.roti_page.get_attribute(RotiKit.SpecialRotiLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelBakhri(self):
        self.roti_page.click_OrderRotiKit()
        label = self.roti_page.get_attribute(RotiKit.BakhriLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_labelWhatWeDeliver(self):
        label = self.roti_page.get_attribute(RotiKit.whatweDeliver, 'innerHTML')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_labelFresh(self):
        label = self.roti_page.get_attribute(RotiKit.FreshHomeMade, 'innerHTML')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_labelPremium(self):
        label = self.roti_page.get_attribute(RotiKit.Premium, 'innerHTML')
        print(label)
        self.assertEqual(self.actual16, label)

    def test_labelFreeDelivery(self):
        label = self.roti_page.get_attribute(RotiKit.FreeDeivery, 'innerHTML')
        print(label)
        self.assertEqual(self.actual17, label)

    def test_labelWhatAreRotis(self):
        label = self.roti_page.get_attribute(RotiKit.WhatareRotis, 'innerHTML')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_weekly(self):
        self.roti_page.click_weekly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.weekly.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual19, hex)

    def test_clickbiweekly(self):
        self.roti_page.click_OrderRotiKit()
        self.roti_page.click_Biweekly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.bi-weekly.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual19, hex)

    def test_monthly(self):
        # self.roti_page.click_OIG()
        self.roti_page.click_Monthly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.monthly.tablinks').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual19, hex)

    def test_once(self):
        self.roti_page.click_Once()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > section.productsection > div > div > div.organicproductcontent > div.divcustomtabpanels > ul > li.one-time.tablinks.active').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual19, hex)

    def test_labelFreeDeliveryOnMinimumOrder(self):
        label = self.roti_page.get_attribute(RotiKit.FreeDeiveryOnMinimumOrder, 'innerHTML')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_clickwholeWheat(self):
        self.roti_page.click_OrderRotiKit()
        self.roti_page.click_WholeWheat()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_clickroti(self):
        self.roti_page.click_OrderRotiKit()
        self.roti_page.click_roti()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_clickmultiGrain(self):
        self.roti_page.click_OrderRotiKit()
        self.roti_page.click_multiGrain()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_clickrotla(self):
        self.roti_page.click_OrderRotiKit()
        self.roti_page.click_rotla()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_clickparatha(self):
        self.roti_page.click_OrderRotiKit()
        self.roti_page.click_Paratha()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_clickspecialRoti(self):
        self.roti_page.click_OrderRotiKit()
        self.roti_page.click_SpecialRoti()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_clickbakhri(self):
        self.roti_page.click_Bakhri()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_clickbuildABox(self):
        self.roti_page.click_buildABox()
        label = self.roti_page.get_attribute(RotiKit.IndianBread, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)
