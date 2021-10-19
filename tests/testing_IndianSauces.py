import time
from resources import ui_test_class
from resources.page_objects.IndianSauces import IndianMealKitAndSauces
from resources.page_objects.IndianSauces import Sauces
from selenium.webdriver.support.color import Color


class TesINDIANSAUCES(ui_test_class.UVXVXVClass):
    sauces_page: IndianMealKitAndSauces
    sauces_page: Sauces

    actual1 = "EXPLORE OUR MENUS"
    actual2 = "Instant Pot Chicago IL"
    actual3 = "Search for products..."
    actual4 = "Sauces"
    actual5 = "Meal Kit"
    actual6 = "EFFORTLESS COOKING: HOW IT WORKS?"
    actual7 = "Step 1."
    actual8 = "Step 2."
    actual9 = "Step 3."
    actual10 = "Step 4."
    actual11 = "From Fridge to Pot: 2 - 3 mins"
    actual12 = "Set Pot to Cook: 1 min"
    actual13 = "Relax: 15+ mins"
    actual14 = "Enjoy!"
    actual15 = "OUR FOOD PHILOSOPHY"
    actual16 = " Indian Food Subscription Box"
    actual17 = "Nationwide"
    actual18 = "Bay Area"
    actual19 = "#000000"
    actual20 = "Sauces"
    actual21 = "Meal Kit"
    actual22 = "Eat Everything"
    actual23 = "Vegetarian Meal Kit"
    actual24 = "Vegan Meal Kit"
    actual25 = "Nut Free Meal Kit"
    actual26 = "Bay Area"

    @classmethod
    def setUpClass(cls):
        super(TesINDIANSAUCES, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesINDIANSAUCES, cls).tearDownClass()
        cls.driver.quit()

    def test_EnterZipCode(self):
        self.sauces_page.zip("60611")
        self.sauces_page.submit_zip()
        search = self.sauces_page.get_attribute(IndianMealKitAndSauces.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_clickIndian(self):
        for i in range(3):
            time.sleep(1)
            self.sauces_page.click_RightArrow()
        self.sauces_page.click_MealKit()
        self.sauces_page.click_sauces()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.instantPot, 'innerHTML')
        print(label)
        self.assertEqual(self.actual2, label)

    def test_labelExplore(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.explore, 'innerHTML')
        print(label)
        self.assertEqual(self.actual1, label)

    def test_labelSauces(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.sauces, 'innerHTML')
        print(label)
        self.assertEqual(self.actual4, label)

    def test_labelMealKit(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.mealKit, 'innerHTML')
        print(label)
        self.assertEqual(self.actual5, label)

    def test_labelEffortless(self):
        self.sauces_page.click_NationWide()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.effortless, 'innerHTML')
        print(label)
        self.assertEqual(self.actual6, label)

    def test_labelStep1(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step1, 'innerHTML')
        print(label)
        self.assertEqual(self.actual7, label)

    def test_labelStep2(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step2, 'innerHTML')
        print(label)
        self.assertEqual(self.actual8, label)

    def test_labelStep3(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step3, 'innerHTML')
        print(label)
        self.assertEqual(self.actual9, label)

    def test_labelStep4(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.step4, 'innerHTML')
        print(label)
        self.assertEqual(self.actual10, label)

    def test_labelFridge(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.fromFridge, 'innerHTML')
        print(label)
        self.assertEqual(self.actual11, label)

    def test_labelSetPan(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.setPan, 'innerHTML')
        print(label)
        self.assertEqual(self.actual12, label)

    def test_labelRelax(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.relax, 'innerHTML')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_labelEnjoy(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.enjoy, 'innerHTML')
        print(label)
        self.assertEqual(self.actual14, label)

    def test_labelPhilosophy(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.OurFoodPhilosophy, 'innerHTML')
        print(label)
        self.assertEqual(self.actual15, label)

    def test_labelDelivery(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.delivery, 'textContent')
        print(label)
        # self.assertEqual(self.actual16, label)

    def test_labelNationWide(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.nationwide, 'innerHTML')
        print(label)
        self.assertEqual(self.actual17, label)

    def test_labelBayArea(self):
        self.sauces_page.click_backToPage()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.BayArea, 'innerHTML')
        print(label)
        self.assertEqual(self.actual18, label)

    def test_clickbayArea(self):
        self.sauces_page.click_BayArea()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > div.clsTiffinMenus > ul > li:nth-child(2) > a').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual19, hex)

    def test_clicknationWide(self):
        self.sauces_page.click_Bay()
        self.sauces_page.click_NationWide()
        colorLabel = self.driver.find_element_by_css_selector(
            '#searchhide > div.clsTiffinMenus > ul > li.selected > a').value_of_css_property(
            'background-color')
        hex = Color.from_string(colorLabel).hex
        print(hex)
        self.assertEqual(self.actual19, hex)

    def test_clickselect(self):
        self.sauces_page.click_backToPage()
        self.sauces_page.click_select()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.saucesLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual20, label)

    def test_clickselect1(self):
        self.sauces_page.click_backToPage()
        self.sauces_page.click_select1()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.mealKitLabel, 'innerHTML')
        print(label)
        self.assertEqual(self.actual21, label)

    def test_labelEatEverything(self):
        self.sauces_page.click_BayArea()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.Eat, 'innerHTML')
        print(label)
        self.assertEqual(self.actual22, label)

    def test_labelVegetarian(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.vegetarian, 'innerHTML')
        print(label)
        self.assertEqual(self.actual23, label)

    def test_labelVegan(self):
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.vegan, 'innerHTML')
        print(label)
        self.assertEqual(self.actual24, label)

    def test_labelNutFree(self):
        self.sauces_page.click_BayArea()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.NutFree, 'innerHTML')
        print(label)
        self.assertEqual(self.actual25, label)

    def test_clickeat(self):
        self.sauces_page.click_Eat()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
        print(label)
        self.assertEqual(self.actual26, label)

    def test_clickvegetarian(self):
        self.sauces_page.click_Bay()
        self.sauces_page.click_BayArea()
        self.sauces_page.click_Vegetarian()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
        print(label)
        self.assertEqual(self.actual26, label)

    def test_clickvegan(self):
        self.sauces_page.click_Bay()
        self.sauces_page.click_BayArea()
        self.sauces_page.click_Vegan()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
        print(label)
        self.assertEqual(self.actual26, label)

    def test_clicknut(self):
        self.sauces_page.click_BayArea()
        self.sauces_page.click_Nut()
        label = self.sauces_page.get_attribute(IndianMealKitAndSauces.clickBay, 'innerHTML')
        print(label)
        self.assertEqual(self.actual26, label)


