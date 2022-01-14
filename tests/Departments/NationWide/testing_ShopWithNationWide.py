import time
from resources import ui_test_class
from resources.page_objects.department import Department
from resources.page_objects.department import Dept
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TesDEPARTMENT(ui_test_class.UVIIClass):
    depart_page: Dept
    depart_page: Department

    actual1 = "Thank you"
    actual2 = "Your Account"
    actual3 = "Search for products..."

    @classmethod
    def setUpClass(cls):
        super(TesDEPARTMENT, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesDEPARTMENT, cls).tearDownClass()
        cls.driver.quit()

    def NationWideShop(self):
        time.sleep(5)
        self.depart_page.click_NationWideShop()
        time.sleep(5)
        self.depart_page.click_MealKit()
        # self.depart_page.click_IndianMealKit()
        time.sleep(10)
        self.depart_page.click_SelectProducts()
        time.sleep(10)
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(Department.AddMisalPav))
        #wait = WebDriverWait(driver, 10)
        #element = wait.until(EC.element_to_be_clickable((By.')))
        self.depart_page.click_AddMisalPav() #doesnt add
        for i in range(9):
            self.depart_page.click_PlusMixVegetable()
        time.sleep(2)
        self.depart_page.click_AddToCartNW()
        time.sleep(2)
        self.depart_page.click_MiniCart()
        self.depart_page.click_Checkout()
        self.depart_page.click_Checkout2()
        self.depart_page.click_payment1()
        time.sleep(5)
        self.depart_page.click_Pay()
        time.sleep(10)


    def test_EnterZipCode(self):
        self.depart_page.zip("60611")
        self.depart_page.submit_zip()
        search = self.depart_page.get_attribute(Department.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)


    def test_shopWithNationWideShop(self):
        self.NationWideShop()
        ThankYouLabel = self.depart_page.get_attribute(Department.ThankYou, 'innerHTML')
        print(ThankYouLabel)
        self.assertEqual(self.actual1, ThankYouLabel)

