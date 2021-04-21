# from resources import ui_test_class
# from resources.page_objects.cart import MiniCart
# from resources.page_objects.cart import Cart
# import HtmlTestRunner
# import unittest
#
#
# class TesCART(ui_test_class.UVClass):
#     cart_page: Cart
#     cart_page: MiniCart
#
#     @classmethod
#     def setUpClass(cls):
#         super(TesCART, cls).setUpClass()
#
#     @classmethod
#     def tearDownClass(cls):
#         super(TesCART, cls).tearDownClass()
#         cls.driver.quit()
#
#     def setUp(self):
#         super(TesCART, self).setUp()
#         self.base_page.driver.refresh()
#
#     def test_ZipCode(self):
#         self.cart_page.zip("54000")
#         self.cart_page.submit_zip()
#         # self.assertTrue(self.cart_page.zip('54000'))
#
#     def test_EmptyCart(self):
#         self.cart_page.click_cart()
#         empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
#         print(empty)
#
#     def test_click_ProceedCheckOut(self):
#         # self.cart_page.click_cart()
#         # empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
#         # print(empty)
#         self.cart_page.click_select()
#         self.cart_page.click_AddToCart()
#         CheckOut_button = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
#         print(CheckOut_button)
#
#
