from resources import ui_test_class
# import unittest
from resources.page_objects.cart import MiniCart
from resources.page_objects.cart import Cart


# import time


class TesCART(ui_test_class.UVClass):
    cart_page: Cart
    cart_page: MiniCart
    actual1 = "Your cart is empty"
    actual2 = '1 item'

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

    def ZipCode(self):
        self.cart_page.zip("54000")
        self.cart_page.submit_zip()

    def AddToCart(self):
        self.cart_page.click_AddToCart()

    def click_ProceedCheckOut(self):
        self.cart_page.click_select()
        self.cart_page.click_AddToCart()
        self.cart_page.click_MiniCart()
        CheckOut_button = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
        print(CheckOut_button)

    def test_EmptyCart(self):
        self.cart_page.click_MiniCart()
        empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
        # print(empty)
        self.assertEqual(self.actual1, empty, msg="Value is True")

    def test_countItem(self):
        self.cart_page.click_MiniCart()
        ItemNumber = self.cart_page.get_attribute(MiniCart.ItemCount, 'innerHTML')
        print(ItemNumber)
        self.assertEqual(self.actual2, ItemNumber)

    def test_PriceOfItem(self):
        self.cart_page.click_MiniCart()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)

    def test_img(self):
        self.cart_page.click_MiniCart()
        imageSource = self.cart_page.get_attribute(MiniCart.image, 'src')
        print(imageSource)

    def test_NameOfItem(self):
        self.cart_page.click_MiniCart()
        NameOfItem = self.cart_page.get_attribute(MiniCart.NameOfItem, 'innerHTML')
        print(NameOfItem)

    def test_Item_Quantity(self):
        self.cart_page.click_MiniCart()
        self.AddToCart()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)

    def test_MinOrder(self):
        self.cart_page.click_MiniCart()
        MinimumOrder = self.cart_page.find_element(MiniCart.min_order).get_attribute('innerHTML')
        print(MinimumOrder)

    def test_ShopTotal(self):
        self.cart_page.click_MiniCart()
        Total = self.cart_page.find_element(MiniCart.shop_total).get_attribute('innerHTML')
        print(Total)

    def test_PlusMinusQuantity(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_plus()
        self.cart_page.click_minus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)

    def test_shopName(self):
        self.cart_page.click_MiniCart()
        ShopName = self.cart_page.get_attribute(MiniCart.shop_name, 'innerHTML')
        print(ShopName)

    def test_DeleteItem(self):
        self.ZipCode()
        self.click_ProceedCheckOut()
        self.cart_page.click_delete()
        self.cart_page.click_MiniCart()

    def test_UpdatedPrice(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_plus()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)

        # self.assertTrue(self.cart_page.click_MiniCart())

# #
# ++++
#     def test_countItemAndPriceOfItem(self):
#
#         self.cart_page.click_cart()
#         ItemNumber = self.cart_page.get_attribute(MiniCart.ItemCount, 'innerHTML')
#         print(ItemNumber)
#         ItemPrice = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
#         print(ItemPrice)
#
#     def test_imageAndItemQuantity(self):
#
#         self.cart_page.click_cart()
#         imageSource = self.cart_page.get_attribute(MiniCart.image, 'src')
#         print(imageSource)
#         self.cart_page.click_plus()
#         ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
#         print(ItemQuantity)
#
#     def test_name_of_itemAndMinOrder(self):
#
#         self.cart_page.click_cart()
#         NameOfItem = self.cart_page.get_attribute(MiniCart.NameOfItem, 'innerHTML')
#         print(NameOfItem)
#         MinimumOrder = self.cart_page.find_element(MiniCart.min_order).get_attribute('innerHTML')
#         print(MinimumOrder)
#         self.cart_page.click_delete()
#
#     def test_DeleteItem(self):
#         # self.cart_page.click_cart()
#         self.cart_page.click_delete()
#
#     def test_PlusQuantity(self):
#         self.cart_page.click_cart()
#
#
#         self.cart_page.click_plus()
