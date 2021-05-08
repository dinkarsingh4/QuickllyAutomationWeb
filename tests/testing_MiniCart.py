from resources import ui_test_class
from resources.page_objects.cart import MiniCart
from resources.page_objects.cart import Cart


# import unittest
#

class TesCART(ui_test_class.UVClass):
    cart_page: Cart
    cart_page: MiniCart
    actual1 = "Your cart is empty"
    actual2 = "Proceed to Checkout"
    actual3 = '1 item'
    actual4 = "Shop Seeti Min. Order $10"
    actual5 = "Kali Dal"
    actual6 = "1"
    actual7 = "$11.99"
    actual8 = "Shop Seeti Total: $11.99"
    actual9 = "$23.98"
    actual10 = "https://www.quicklly.com/upload_images/product/1618183722-kali-dal.jpg"
    actual11 = "Shop Seeti"
    actual12 = "20"
    actual13 = "Your Shopping Carts"
    actual14 = "Seeti"
    actual15 = "$43.28"
    actual16 = "3"
    actual17 = "$19.3"
    actual18 = "CurbsidePickup"
    actual19 = "Delivery"


    @classmethod
    def setUpClass(cls):
        super(TesCART, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TesCART, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        super(TesCART, self).setUp()
        self.base_page.driver.refresh()

    def test_ZipCode(self):
        self.cart_page.zip("60610")
        self.cart_page.submit_zip()
        self.cart_page.click_MiniCart()
        empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
        print(empty)

    def test_checkout(self):
        check = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
        print(check)

    def test_name(self):
        self.cart_page.click_MiniCart()
        NameOfItem = self.cart_page.get_attribute(MiniCart.NameOfItem, 'innerHTML')
        print(NameOfItem)
        # self.assertEqual(self.actual5, NameOfItem)

    def test_price(self):
        self.cart_page.click_MiniCart()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)
        # self.assertEqual(self.actual7, price)

    def test_image(self):
        imageSource = self.cart_page.get_attribute(MiniCart.image, 'src')
        print(imageSource)
        # self.assertEqual(self.actual10, imageSource)

    def test_count(self):
        self.cart_page.click_MiniCart()
        ItemNumber = self.cart_page.get_attribute(MiniCart.ItemCount, 'innerHTML')
        print(ItemNumber)
        # self.assertEqual(self.actual3, ItemNumber)

    def test_quantity(self):
        self.cart_page.click_MiniCart()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        # self.assertEqual(self.actual6, ItemQuantity)

    def test_minimum(self):
        self.cart_page.click_MiniCart()
        MinimumOrder = self.cart_page.find_element(MiniCart.min_order).get_attribute('innerHTML')
        print(MinimumOrder)
        # self.assertEqual(self.actual4, MinimumOrder)

    def test_total(self):
        self.cart_page.click_MiniCart()
        Total = self.cart_page.find_element(MiniCart.shop_total).get_attribute('innerHTML')
        print(Total)
        # self.assertEqual(self.actual8, Total)

    def test_plus_minus(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_plus()
        self.cart_page.click_minus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        # self.assertEqual(self.actual6, ItemQuantity)

    def test_shops(self):
        self.cart_page.click_MiniCart()
        ShopName = self.cart_page.get_attribute(MiniCart.shop_name, 'innerHTML')
        print(ShopName)
        # self.assertEqual(self.actual11, ShopName)

    def test_updateP(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_plus()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)
        # self.assertEqual(self.actual9, price)

    def test_min(self):
        self.cart_page.click_MiniCart()
        for i in range(19):
            self.cart_page.click_minus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        # self.assertEqual(self.actual6, ItemQuantity)
        print("Item with minimum quantity is added")

    def test_max(self):
        self.cart_page.click_MiniCart()
        for i in range(19):
            self.cart_page.click_plus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        # self.assertEqual(self.actual12, ItemQuantity)
        print("Item with maximum quantity is added")

    def test_shopping(self):
        # self.cart_page.click_MiniCart()
        # self.cart_page.click_CheckOut()
        label = self.cart_page.get_attribute(MiniCart.shopping_carts, 'innerHTML')
        print(label)
        # self.assertEqual(self.actual13, label)

    def test_stores(self):
        label2 = self.cart_page.get_attribute(MiniCart.allStores, 'src')
        print(label2)

    def test_label(self):
        label3 = self.cart_page.get_attribute(MiniCart.shops_name, 'src')
        label4 = self.cart_page.get_attribute(MiniCart.shops_name1, 'src')
        print(label3)
        print(label4)
        # self.assertEqual(self.actual14, label3)

    def test_priceAndCount(self):
        price_label = self.cart_page.get_attribute(MiniCart.price_label, 'innerHTML')
        count_label = self.cart_page.get_attribute(MiniCart.count_label, 'innerHTML')
        print(price_label)
        print(count_label)
        # self.assertEqual(self.actual15, price_label)
        # self.assertEqual(self.actual16, count_label)

    def test_priceEachShop(self):
        price1 = self.cart_page.get_attribute(MiniCart.price1, 'innerHTML')
        price2 = self.cart_page.get_attribute(MiniCart.price2, 'innerHTML')
        print(price1, price2)
        # self.assertEqual(self.actual7, price1)
        # self.assertEqual(self.actual17, price2)

    def test_pickup(self):
        pickup_label = self.cart_page.get_attribute(MiniCart.CurbsidePickup, 'innerHTML')
        print(pickup_label)
        # self.assertEqual(self.actual18, pickup_label)

    def test_delivery(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_Checkout()
        self.cart_page.EnterEmail("testaccount@quicklly.com")
        self.cart_page.EnterPass("123456")
        self.cart_page.click_login()
        delivery_label = self.cart_page.get_attribute(MiniCart.Delivery, 'innerHTML')
        print(delivery_label)

        # self.assertEqual(self.actual19, delivery_label)

    def test_arrow1(self):
        self.cart_page.click_additem()
        self.cart_page.click_AddItem1()
        self.cart_page.click_item()
        self.cart_page.click_Additem2()
        self.cart_page.click_MiniCart()
        self.cart_page.click_rightArrow()

    def test_arrow2(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_leftArrow()

    def test_items(self):
        itemsInCart = self.cart_page.get_attribute(MiniCart.ItemInCart, 'innerHTML')
        print(itemsInCart)

    def test_dropdown1(self):
        self.cart_page.click_dropDown1()

    def test_dropdown2(self):
        self.cart_page.click_dropDown2()

    def test_remove(self):
        RemoveLabel1 = self.cart_page.get_attribute(MiniCart.remove1, 'innerHTML')
        RemoveLabel2 = self.cart_page.get_attribute(MiniCart.remove2, 'innerHTML')
        print(RemoveLabel1, RemoveLabel2)


#     def test_click_ProceedCheckOut(self):
#         # self.cart_page.click_cart()
#         # empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
#         # print(empty)
#         self.cart_page.click_select()
#         self.cart_page.click_AddToCart()
#         CheckOut_button = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
#         print(CheckOut_button)
