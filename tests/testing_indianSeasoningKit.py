import time
from resources import ui_test_class
from resources.page_objects.indianseasoningkit import Indian
from resources.page_objects.indianseasoningkit import IndianSeasoningKit
from selenium.webdriver.support.color import Color


class TesINDIANSEASONING(ui_test_class.UVXVXIClass):
    indian_page: Indian
    indian_page: IndianSeasoningKit

    actual1 = " CHOOSE YOUR MENU"
    actual2 = " Indian Seasoning Kit"
    actual3 = "Search for products..."
    actual4 = "Flavors so familiar, Yet so different."
    actual5 = "https://www.uat.quicklly.com/images/seasoning_kit/Assets/image%2014.png"
    actual6 = "https://www.uat.quicklly.com/images/seasoning_kit/Assets/image%2013.png"
    actual7 = "https://www.uat.quicklly.com/images/seasoning_kit/Assets/image%2015.png"
    actual8 = "https://www.uat.quicklly.com/images/seasoning_kit/Assets/image%2017.png"
    actual9 = "https://www.uat.quicklly.com/images/seasoning_kit/Assets/image%2020.png"
    actual10 = "https://www.uat.quicklly.com/images/seasoning_kit/Assets/image%2016.png"
    actual11 = "Indian Seasoning"
    actual12 = "Easy Indie Bowls"
    actual13 = "#f9660d"
    actual14 = "Seasonings Kit"
    actual15 = "Easy Indie Bowl Kit"
    actual16 = " Order Seasoning Kit"
    actual17 = " Easy Indie Bowl"

    @classmethod
    def setUpClass(cls):
        super(TesINDIANSEASONING, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANSEASONING, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.indian_page.zip("60611")
        self.indian_page.submit_zip()
        search = self.indian_page.get_attribute(IndianSeasoningKit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        for i in range(3):
            time.sleep(1)
            self.indian_page.click_RightArrow()
        self.indian_page.click_MealKit()
        self.indian_page.click_indianSeasoning()
        label = self.indian_page.get_attribute(IndianSeasoningKit.IndianSeasoningLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_labelchooseyourmenu(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.chooseyourmenu, 'innerHTML')
        print(label)
        self.assertEqual(self.actual1, label)

    def test_flavour(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.flavours, 'textContent')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_imageBlackPepper(self):
        image = self.indian_page.get_attribute(IndianSeasoningKit.blackPepperImage, 'src')
        print(image)
        self.assertEqual(self.actual5, image)

    def test_imageStarFlower(self):
        image = self.indian_page.get_attribute(IndianSeasoningKit.startFLowerImage, 'src')
        print(image)
        self.assertEqual(self.actual6, image)

    def test_imageElaichi(self):
        image = self.indian_page.get_attribute(IndianSeasoningKit.ElaichiImage, 'src')
        print(image)
        self.assertEqual(self.actual7, image)

    def test_imageTurmeric(self):
        image = self.indian_page.get_attribute(IndianSeasoningKit.turmericImage, 'src')
        print(image)
        self.assertEqual(self.actual8, image)

    def test_imageNutmeg(self):
        image = self.indian_page.get_attribute(IndianSeasoningKit.nutmegImage, 'src')
        print(image)
        self.assertEqual(self.actual9, image)

    def test_imageCuminSeed(self):
        image = self.indian_page.get_attribute(IndianSeasoningKit.CuminSeedImage, 'src')
        print(image)
        self.assertEqual(self.actual10, image)

    def test_labelIndianSeasoning(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.ISL, 'innerHTML')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelEasyIndieBowls(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.easyIndieBowls, 'innerHTML')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_clickweekly(self):
        self.indian_page.click_ISK()
        self.indian_page.click_weekly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(1) > center > ul > li:nth-child(2)').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_clickbiweekly(self):
        self.indian_page.click_Biweekly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(1) > center > ul > li:nth-child(3)').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_clickmonthly(self):
        self.indian_page.click_Monthly()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(1) > center > ul > li:nth-child(4)').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_clickonce(self):
        self.indian_page.click_Once()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(1) > center > ul > li.active').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_clickweekly1(self):
        self.indian_page.click_weekly2()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(2) > center > ul > li:nth-child(2)').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_clickbiweekly2(self):
        self.indian_page.click_Biweekly2()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(2) > center > ul > li:nth-child(3)').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_clickmonthly2(self):
        self.indian_page.click_Monthly2()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(2) > center > ul > li.active').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_clickonce2(self):
        self.indian_page.click_Once2()
        colorLabel = self.driver.find_element_by_css_selector(
            '#seasn1 > div:nth-child(2) > center > ul > li:nth-child(1)').value_of_css_property('background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual13, hex)

    def test_labelSeasoningKit(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.seasoningKitLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_labelEasyIndianBowlKit(self):
        label = self.indian_page.get_attribute(IndianSeasoningKit.EasyIndianLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_clickselectProducts(self):
        self.indian_page.click_selectProduct()
        label = self.indian_page.get_attribute(IndianSeasoningKit.OrderSeasoningKit, 'innerHTML')
        print(label)
        self.assertEqual(self.actual16, label)

    def test_clickselectProducts2(self):
        self.indian_page.click_ISK()
        self.indian_page.click_selectProduct2()
        label = self.indian_page.get_attribute(IndianSeasoningKit.labelEasy, 'innerHTML')
        print(label)
        self.assertEqual(self.actual17, label)

