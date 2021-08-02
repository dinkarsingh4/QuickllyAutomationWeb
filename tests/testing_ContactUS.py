from resources import ui_test_class
from resources.locators import Contact
from resources.page_objects.contact_us import contactUs


class TesCONTACTUS(ui_test_class.UVIXClass):
    contact_page: Contact
    contact_page: contactUs

    @classmethod
    def setUpClass(cls):
        super(TesCONTACTUS, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCONTACTUS, cls).tearDownClass()
        cls.driver.quit()

    def test_zipcode(self):
        self.contact_page.zip("60070")
