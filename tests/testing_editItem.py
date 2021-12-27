import time
from resources import ui_test_class
from resources.page_objects.edit_page import EDITITEM
from resources.page_objects.edit_page import Edit


class TesEDITITEM(ui_test_class.UVXVXVVIIClass):
    edit_page: Edit
    edit_page: EDITITEM

    actual1 = "Thank you"
    actual3 = "Search for products..."
    actual2 = "Logout"
    text = ""

    @classmethod
    def setUpClass(cls):
        super(TesEDITITEM, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesEDITITEM, cls).tearDownClass()
        cls.driver.quit()

    def edit(self):
        time.sleep(2)
        self.edit_page.click_NationWideShop()
        self.edit_page.click_indianSweet()
        self.edit_page.click_monthly()
        self.edit_page.click_buildABox()
        self.edit_page.click_addMasalaMathai()
        for i in range(4):
            self.edit_page.click_plusMasalaMathai()
        self.edit_page.click_deleteItem()

    def test_EnterZipCode(self):
        self.edit_page.zip("60611")
        self.edit_page.submit_zip()
        search = self.edit_page.get_attribute(Edit.SearchForProducts, 'placeholder')
        print(search)
        self.assertEqual(self.actual3, search)

    def test_SignIn(self):
        self.edit_page.select_dropdown()
        self.edit_page.click_signin()
        self.edit_page.EnterEmail("testaccount@quicklly.com")
        self.edit_page.EnterPass("123456")
        self.edit_page.click_login()
        self.edit_page.select_dropdown()
        logoutLabel = self.edit_page.get_attribute(Edit.logout, 'innerHTML')
        print(logoutLabel)
        self.assertEqual(self.actual2, logoutLabel)

    def test_editItem(self):
        self.edit()
