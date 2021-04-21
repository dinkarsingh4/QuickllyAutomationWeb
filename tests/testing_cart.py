from resources import ui_test_class
import HtmlTestRunner
import unittest
from resources.page_objects.cart import MiniCart
from resources.page_objects.cart import Cart
# from selenium import webdriver


# import time


class TesCART(ui_test_class.UVClass):
    cart_page: Cart
    cart_page: MiniCart

    @classmethod
    def setUpClass(cls):
        super(TesCART, cls).setUpClass()
        # cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        super(TesCART, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        super(TesCART, self).setUp()
        self.base_page.driver.refresh()

    def test_ZipCode(self):

        self.cart_page.zip("54000")
        self.cart_page.submit_zip()

    def test_click_ProceedCheckOut(self):
        self.cart_page.click_cart()
        empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
        print(empty)
        self.cart_page.click_select()
        self.cart_page.click_AddToCart()
        CheckOut_button = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
        print(CheckOut_button)


    def test_countItemAndPriceOfItem(self):

        self.cart_page.click_cart()
        ItemNumber = self.cart_page.get_attribute(MiniCart.ItemCount, 'innerHTML')
        print(ItemNumber)
        ItemPrice = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(ItemPrice)

    def test_imageAndItemQuantity(self):

        self.cart_page.click_cart()
        imageSource = self.cart_page.get_attribute(MiniCart.image, 'src')
        print(imageSource)
        self.cart_page.click_plus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)

    def test_name_of_itemAndMinOrder(self):

        self.cart_page.click_cart()
        NameOfItem = self.cart_page.get_attribute(MiniCart.NameOfItem, 'innerHTML')
        print(NameOfItem)
        MinimumOrder = self.cart_page.find_element(MiniCart.min_order).get_attribute('innerHTML')
        print(MinimumOrder)
        self.cart_page.click_delete()

    # def test_DeleteItem(self):
    #     # self.cart_page.click_cart()
    #     self.cart_page.click_delete()

    # def test_PlusQuantity(self):
    #     self.cart_page.click_cart()
    #
    #
    #     self.cart_page.click_plus()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports', report_title='Cart'))
