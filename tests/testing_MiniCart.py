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
    actual3 = '2 items'
    actual4 = "Fresh Farms Min. Order $30"
    actual5 = "LEMON GRASS"
    actual6 = "1"
    actual7 = "$0.59"
    actual8 = "Fresh Farms Total: $1.18"
    actual9 = "$1.77"
    actual10 = "https://www.quicklly.com/upload_images/product/thumb/1495539333-lemon-grass.jpg"
    actual11 = "Fresh Farms"
    actual12 = "20"
    actual13 = "Your Shopping Carts"
    actual14 = "Seeti"
    actual15 = "$0.29"
    actual16 = "3"
    actual17 = "$0.88"
    actual18 = "Curbside Pickup"
    actual19 = "Delivery"
    actual20 = "eVoucher"
    actual21 = "https://www.quicklly.com/images/allstores.png"
    actual22 = "https://www.quicklly.com/seller/upload_images/store/thumb/ff.png"
    actual23 = "https://www.quicklly.com/seller/upload_images/store/thumb/1601044053-campus-market.png"
    actual24 = "(2 item)"
    actual25 = "Items in your  cart"
    actual26 = "Remove"
    actual27 = "eVoucher"
    actual28 = "Reward Point (0)"
    actual29 = "My Wallet"
    actual30 = "Your e-voucher Code option"
    actual31 = " * A maximum of one vouher is applicable for an order"
    actual32 = "Your Reward Point (optional)*"
    actual34 = "Your Wallet Balance (optional)*"
    actual33 = " * Reward Point applicable"
    actual35 = "Your Wallet is empty"
    actual36 = "Order Summary"
    actual37 = "(2 items)"
    actual38 = "Groceries Subtotal (2 items)"
    actual39 = "Food Subtotal (0 item)"
    actual40 = "(0 item)"
    actual41 = "$0.00"
    actual42 = "Estimated Tax"
    actual43 = "Estimated Shipping"
    actual44 = "$4.99"
    actual45 = "Estimated Minimum Charges"
    actual46 = "$5.98"
    actual47 = "Packaging Handling"
    actual48 = "$0.99"
    actual49 = "Tip"
    actual50 = "$0.06"
    actual51 = "Estimated Order Total"
    actual52 = "12.95"
    actual53 = "Delivery:"
    actual54 = "Change Address"

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

    def AddItem(self):
        self.cart_page.click_additem()
        self.cart_page.click_AddItem1()
        self.cart_page.click_item()
        self.cart_page.click_Additem2()

    def test_ZipCode(self):
        self.cart_page.zip("60610")
        self.cart_page.submit_zip()
        self.cart_page.click_MiniCart()
        empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
        print(empty)

    def test_checkout(self):
        check = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
        print(check)
        self.assertEqual(self.actual2, check)

    def test_name(self):
        self.cart_page.click_MiniCart()
        NameOfItem = self.cart_page.get_attribute(MiniCart.NameOfItem, 'innerHTML')
        print(NameOfItem)
        self.assertEqual(self.actual5, NameOfItem)

    def test_price(self):
        self.cart_page.click_MiniCart()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)
        self.assertEqual(self.actual7, price)

    def test_image(self):
        imageSource = self.cart_page.get_attribute(MiniCart.image, 'src')
        print(imageSource)
        self.assertEqual(self.actual10, imageSource)

    def test_count(self):
        self.cart_page.click_MiniCart()
        ItemNumber = self.cart_page.get_attribute(MiniCart.ItemCount, 'innerHTML')
        print(ItemNumber)
        self.assertEqual(self.actual3, ItemNumber)

    def test_quantity(self):
        self.cart_page.click_MiniCart()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        self.assertEqual(self.actual6, ItemQuantity)

    def test_minimum(self):
        self.cart_page.click_MiniCart()
        MinimumOrder = self.cart_page.find_element(MiniCart.min_order).get_attribute('innerHTML')
        print(MinimumOrder)
        self.assertEqual(self.actual4, MinimumOrder)

    def test_total(self):
        self.cart_page.click_MiniCart()
        Total = self.cart_page.find_element(MiniCart.shop_total).get_attribute('innerHTML')
        print(Total)
        self.assertEqual(self.actual8, Total)

    def test_plus_minus(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_plus()
        self.cart_page.click_minus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        self.assertEqual(self.actual6, ItemQuantity)

    def test_shops(self):
        self.cart_page.click_MiniCart()
        ShopName = self.cart_page.get_attribute(MiniCart.shop_name, 'innerHTML')
        print(ShopName)
        self.assertEqual(self.actual11, ShopName)

    def test_updateP(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_plus()
        price = self.cart_page.get_attribute(MiniCart.PriceOfItem, 'innerHTML')
        print(price)
        self.assertEqual(self.actual9, price)

    def test_min(self):
        self.cart_page.click_MiniCart()
        for i in range(19):
            self.cart_page.click_minus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        self.assertEqual(self.actual6, ItemQuantity)
        print("Item with minimum quantity is added")

    def test_max(self):
        self.cart_page.click_MiniCart()
        for i in range(19):
            self.cart_page.click_plus()
        ItemQuantity = self.cart_page.get_attribute(MiniCart.ItemQuantity, 'innerHTML')
        print(ItemQuantity)
        self.assertEqual(self.actual12, ItemQuantity)
        print("Item with maximum quantity is added")

    def test_shopping(self):
        label = self.cart_page.get_attribute(MiniCart.shopping_carts, 'innerHTML')
        print(label)
        self.assertEqual(self.actual13, label)

    def test_stores(self):
        label2 = self.cart_page.get_attribute(MiniCart.allStores, 'src')
        print(label2)
        self.assertEqual(self.actual21, label2)

    def test_label(self):
        label3 = self.cart_page.get_attribute(MiniCart.shops_name, 'src')
        label4 = self.cart_page.get_attribute(MiniCart.shops_name1, 'src')
        print(label3)
        print(label4)
        self.assertEqual(self.actual22, label3)
        self.assertEqual(self.actual23, label4)

    def test_priceAndCount(self):
        price_label = self.cart_page.get_attribute(MiniCart.price_label, 'innerHTML')
        count_label = self.cart_page.get_attribute(MiniCart.count_label, 'innerHTML')
        print(price_label)
        print(count_label)
        self.assertEqual(self.actual17, price_label)
        self.assertEqual(self.actual24, count_label)

    def test_priceEachShop(self):
        price1 = self.cart_page.get_attribute(MiniCart.price1, 'innerHTML')
        price2 = self.cart_page.get_attribute(MiniCart.price2, 'innerHTML')
        print(price1, price2)
        self.assertEqual(self.actual7, price1)
        self.assertEqual(self.actual15, price2)

    def test_pickup(self):
        pickup_label = self.cart_page.get_attribute(MiniCart.CurbsidePickup, 'innerHTML')
        print(pickup_label)
        self.assertEqual(self.actual18, pickup_label)

    def test_delivery(self):
        delivery_label = self.cart_page.get_attribute(MiniCart.Delivery, 'innerHTML')
        print(delivery_label)
        self.assertEqual(self.actual19, delivery_label)

    def test_arrow1(self):
        self.AddItem()
        self.cart_page.click_MiniCart()
        self.cart_page.click_rightArrow()
        self.cart_page.click_Checkout()
        self.cart_page.EnterEmail("testaccount@quicklly.com")
        self.cart_page.EnterPass("123456")
        self.cart_page.click_login()
        # self.Login()

    def test_arrow2(self):
        self.cart_page.click_MiniCart()
        self.cart_page.click_leftArrow()

    def test_items(self):
        itemsInCart = self.cart_page.get_attribute(MiniCart.ItemInCart, 'innerHTML')
        print(itemsInCart)
        self.assertEqual(self.actual25, itemsInCart)

    def test_dropdown1(self):
        self.cart_page.click_dropDown1()

    def test_dropdown2(self):
        self.cart_page.click_dropDown2()

    def test_remove(self):
        RemoveLabel1 = self.cart_page.get_attribute(MiniCart.remove1, 'innerHTML')
        RemoveLabel2 = self.cart_page.get_attribute(MiniCart.remove2, 'innerHTML')
        print(RemoveLabel1, RemoveLabel2)
        self.assertEqual(self.actual26, RemoveLabel2)
        self.assertEqual(self.actual26, RemoveLabel1)

    def test_quantity_dropdown(self):
        self.cart_page.click_dropDown1()
        self.cart_page.click_quantity()

    def test_remove_item(self):
        self.cart_page.click_remove()

    def test_voucher(self):
        self.cart_page.click_eVoucher()

    def test_eVoucher_label(self):
        e_label = self.cart_page.get_attribute(MiniCart.eVoucher_label, 'innerHTML')
        print(e_label)
        self.assertEqual(self.actual27, e_label)

    def test_reward(self):
        self.cart_page.click_reward()

    def test_reward_label(self):
        reward_label = self.cart_page.get_attribute(MiniCart.reward_label, 'innerHTML')
        print(reward_label)
        self.assertEqual(self.actual28, reward_label)

    def test_wallet(self):
        self.cart_page.click_wallet()

    def test_wallet_label(self):
        wallet_label = self.cart_page.get_attribute(MiniCart.wallet_label, 'innerHTML')
        print(wallet_label)
        self.assertEqual(self.actual29, wallet_label)

    def test_label_codeOption(self):
        self.cart_page.click_eVoucher()
        CodeOption = self.cart_page.get_attribute(MiniCart.codeOption, 'innerHTML')
        print(CodeOption)
        self.assertEqual(self.actual30, CodeOption)

    def test_text_eVoucher(self):
        self.cart_page.click_eVoucher()
        self.cart_page.enter_eVoucher("12345")

    def test_max_eVoucher(self):
        self.cart_page.click_eVoucher()
        maximum_eVoucher = self.cart_page.get_attribute(MiniCart.maximum_eVoucher, 'innerHTML')
        print(maximum_eVoucher)
        self.assertEqual(self.actual31, maximum_eVoucher)

    def test_rewardPoint(self):
        self.cart_page.click_reward()
        RewardPointLAbel = self.cart_page.get_attribute(MiniCart.rewardPoint, 'innerHTML')
        print(RewardPointLAbel)
        self.assertEqual(self.actual32, RewardPointLAbel)

    # def test_reward_text(self):
    #     self.cart_page.click_reward()
    #     self.cart_page.enter_reward("100")

    def test_rewardPointApplicable(self):
        self.cart_page.click_reward()
        RPA_label = self.cart_page.get_attribute(MiniCart.rewardPointApplicable, 'innerHTML')
        print(RPA_label)
        self.assertEqual(self.actual33, RPA_label)

    def test_walletBalance(self):
        self.cart_page.click_wallet()
        balance = self.cart_page.get_attribute(MiniCart.walletBalance, 'innerHTML')
        print(balance)
        self.assertEqual(self.actual34, balance)

    def test_walletEmpty(self):
        self.cart_page.click_wallet()
        wEmpty = self.cart_page.get_attribute(MiniCart.walletEmpty, 'innerHTML')
        print(wEmpty)
        self.assertEqual(self.actual35, wEmpty)

    def test_order_summary(self):
        summary = self.cart_page.get_attribute(MiniCart.orderSummary, 'innerHTML')
        print(summary)
        self.assertEqual(self.actual36, summary)

    def test_groceries_total(self):
        SubTotal = self.cart_page.get_text(MiniCart.groceriesSubTotal)
        print(SubTotal)
        self.assertEqual(self.actual38, SubTotal)

    def test_groceries_items(self):
        ItemTotal = self.cart_page.get_attribute(MiniCart.groceriesItemTotal, 'innerHTML')
        print(ItemTotal)
        self.assertEqual(self.actual37, ItemTotal)

    def test_grocery_price(self):
        groceriesPrice = self.cart_page.get_attribute(MiniCart.groceriesPrice, 'innerHTML')
        print(groceriesPrice)
        self.assertEqual(self.actual17, groceriesPrice)

    def test_food_total(self):
        subtotal = self.cart_page.get_text(MiniCart.FoodSubTotal)
        print(subtotal)
        self.assertEqual(self.actual39, subtotal)

    def test_food_itemTotal(self):
        ItemTotal = self.cart_page.get_attribute(MiniCart.FoodItemTotal, 'innerHTML')
        print(ItemTotal)
        self.assertEqual(self.actual40, ItemTotal)

    def test_food_price(self):
        FoodPrice = self.cart_page.get_attribute(MiniCart.FoodPrice, 'innerHTML')
        print(FoodPrice)
        self.assertEqual(self.actual41, FoodPrice)

    def test_tax_label(self):
        Estimated = self.cart_page.get_attribute(MiniCart.EstimatedTax, 'innerHTML')
        print(Estimated)
        self.assertEqual(self.actual42, Estimated)

    def test_tax_price(self):
        EstimatedPrice = self.cart_page.get_attribute(MiniCart.EstimatedTaxPrice, 'innerHTML')
        print(EstimatedPrice)

    def test_shipping_estimated(self):
        EstimatedShipping_label = self.cart_page.get_attribute(MiniCart.EstimatedShipping, 'innerHTML')
        print(EstimatedShipping_label)
        self.assertEqual(self.actual43, EstimatedShipping_label)

    def test_shipping_price(self):
        ShippingPrice = self.cart_page.get_attribute(MiniCart.EstimatedShippingPrice, 'innerHTML')
        print(ShippingPrice)
        self.assertEqual(self.actual44, ShippingPrice)

    def test_minimum_charge(self):
        Minimum = self.cart_page.get_attribute(MiniCart.MinimumCharge, 'innerHTML')
        print(Minimum)
        self.assertEqual(self.actual45, Minimum)

    def test_minimum_price(self):
        MinimumPrice = self.cart_page.get_attribute(MiniCart.MinimumChargePrice, 'innerHTML')
        print(MinimumPrice)
        self.assertEqual(self.actual46, MinimumPrice)

    def test_package_handling(self):
        Package = self.cart_page.get_attribute(MiniCart.PackageHandling, 'innerHTML')
        print(Package)
        self.assertEqual(self.actual47, Package)

    def test_package_price(self):
        PackagePrice = self.cart_page.get_attribute(MiniCart.PackageHandlingPrice, 'innerHTML')
        print(PackagePrice)
        self.assertEqual(self.actual48, PackagePrice)

    def test_tip_label(self):
        Tip_label = self.cart_page.get_attribute(MiniCart.Tip, 'innerHTML')
        print(Tip_label)
        self.assertEqual(self.actual49, Tip_label)

    def test_tip_price(self):
        TipPrice = self.cart_page.get_attribute(MiniCart.TipPrice, 'innerHTML')
        print(TipPrice)
        # self.assertEqual(self.actual50, TipPrice)

    def test_no_tip(self):
        self.cart_page.click_NoTIp()

    def test_tip5(self):
        self.cart_page.click_Tip5()

    def test_tipTen(self):
        self.cart_page.click_Tip10()

    def test_tip15(self):
        self.cart_page.click_Tip15()

    def test_tip20(self):
        self.cart_page.click_Tip20()

    def test_estimated_order(self):
        EstimatedOrder = self.cart_page.get_attribute(MiniCart.EstimatedOrder, 'innerHTML')
        print(EstimatedOrder)
        self.assertEqual(self.actual51, EstimatedOrder)

    def test_estimated_order_price(self):
        OrderPrice = self.cart_page.get_attribute(MiniCart.EstimatedOrderPrice, 'innerHTML')
        print(OrderPrice)
        self.assertEqual(self.actual52, OrderPrice)

    def test_delivery_label(self):
        deliveryLabel = self.cart_page.get_attribute(MiniCart.DeliveryLabel, 'innerHTML')
        print(deliveryLabel)
        self.assertEqual(self.actual53, deliveryLabel)

    def test_changeAddressLabel(self):
        ChangeAddress = self.cart_page.get_attribute(MiniCart.ChangeAddress, 'innerHTML')
        print(ChangeAddress)
        self.assertEqual(self.actual54, ChangeAddress)

    # def test_change_address(self):
    #     self.cart_page.click_changeAddress()

    def test_estimatedDelivery(self):
        estimatedDelivery_label = self.cart_page.get_attribute(MiniCart.EstimatedDelivery, 'innerHTML')
        print(estimatedDelivery_label)

    def test_delivery_notes(self):
        notes = self.cart_page.get_attribute(MiniCart.DeliveryNotes, 'innerHTML')
        print(notes)

    def test_notes(self):
        self.cart_page.enter_notes("Please be on time")

    def test_proceedToPayment(self):
        self.cart_page.click_payment()
        payment = self.cart_page.get_attribute(MiniCart.ProceedToPayment, 'innerHTML')
        print(payment)

    def test_invalid_coupon(self):
        self.cart_page.click_eVoucher()
        self.cart_page.enter_eVoucher("12345")
        self.cart_page.click_apply()
        Invalid = self.cart_page.get_attribute(MiniCart.InvalidCoupon, 'innerHTML')
        print(Invalid)

#     def test_click_ProceedCheckOut(self):
#         # self.cart_page.click_cart()
#         # empty = self.cart_page.get_attribute(MiniCart.empty_cart, 'innerHTML')
#         # print(empty)
#         self.cart_page.click_select()
#         self.cart_page.click_AddToCart()
#         CheckOut_button = self.cart_page.get_attribute(MiniCart.proceed_to_checkOut, 'innerHTML')
#         print(CheckOut_button)
