from resources.config_methods import DataClass
from resources.locators import MiniCart
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Cart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def EnterEmail(self, email):
        self.find_elements(MiniCart.Email).clear()
        self.find_element(MiniCart.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(MiniCart.Pass).clear()
        self.find_element(MiniCart.Pass).send_keys(password)

    def click_login(self):
        self.click(MiniCart.LoginButton)

    def click_signin(self):
        self.scroll_to_element(MiniCart.SignInButton)
        self.click(MiniCart.SignInButton)

    def zip(self, zipcode):
        # self.scroll_to_element(MiniCart.enter_zip)
        self.find_elements(MiniCart.enter_zip).clear()
        self.find_element(MiniCart.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        # self.scroll_to_element(MiniCart.submit_zip)
        # # self.scroll_to(492, -542)
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.element_to_be_clickable(MiniCart.submit_zip))
        # element.click()
        self.click(MiniCart.submit_zip)

    def click_MiniCart(self):
        # WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(MiniCart.click_cart)).click()
        # self.wait_for_page_load(15)
        self.scroll_to_element(MiniCart.click_cart)
        self.click(MiniCart.click_cart)

    def Empty_cart(self):
        self.find_element(MiniCart.empty_cart).get_attribute('innerHTML')

    def click_CheckOut(self):
        self.click(MiniCart.proceed_to_checkOut)

    def click_AddToCart(self):
        self.scroll_to_element(MiniCart.Add1)
        self.click(MiniCart.Add1)

    def click_plus(self):
        # self.wait_for_loader(10)
        # self.scroll_to_element(MiniCart.PlusQuantity)
        self.click(MiniCart.PlusQuantity)

    def click_minus(self):
        # self.scroll_to_element(MiniCart.MinusQuantity)
        # self.wait_for_loader(5)
        self.click(MiniCart.MinusQuantity)

    def click_delete(self):
        self.click(MiniCart.delete_item)

    def click_Checkout(self):
        self.click(MiniCart.proceed_to_checkOut)

    def click_additem(self):
        self.scroll_to_element(MiniCart.additem)
        # self.wait(10)
        self.click(MiniCart.additem)

    def click_AddItem1(self):
        self.scroll_to_element(MiniCart.additem2)
        # self.driver.implicitly_wait(20)
        self.click(MiniCart.additem2)

    def click_order(self):
        self.click(MiniCart.orderFood)

    def click_express(self):
        self.click(MiniCart.express)

    def click_item(self):
        self.scroll_to_element(MiniCart.item1)
        self.click(MiniCart.item1)

    def click_additem1(self):
        self.click(MiniCart.additem1)

    def click_Additem2(self):
        self.click(MiniCart.addToCart)

    def click_rightArrow(self):
        self.click(MiniCart.right_arrow)

    def click_leftArrow(self):
        self.click(MiniCart.left_arrow)

    def click_dropDown1(self):
        # self.wait_for_loader(15)
        # self.scroll_to_element(MiniCart.drop_down1)
        self.click(MiniCart.drop_down1)

    def click_dropDown2(self):
        # self.wait_for_loader(15)
        self.click(MiniCart.drop_down2)

    def click_quantity(self):
        # self.wait_for_loader(15)
        self.click(MiniCart.drop_quantity)

    def click_remove(self):
        self.click(MiniCart.remove2)

    def click_eVoucher(self):
        self.scroll_to(1494, -36)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(MiniCart.eVoucher))
        element.click()
        # self.scroll_to_element(MiniCart.eVoucher)
        # self.wait_for_loader(15)
        # self.click(MiniCart.eVoucher)

    def click_reward(self):
        self.click(MiniCart.reward)

    def click_wallet(self):
        self.click(MiniCart.wallet)

    def enter_eVoucher(self, evoucher):
        self.find_elements(MiniCart.eVoucher_text).clear()
        self.find_element(MiniCart.eVoucher_text).send_keys(evoucher)

    def enter_reward(self, reward):
        self.scroll_to_element(MiniCart.reward_text)
        self.wait_for_loader(10)
        self.find_elements(MiniCart.reward_text).clear()
        self.find_element(MiniCart.reward_text).send_keys(reward)

    def click_NoTIp(self):
        self.wait_for_loader(15)
        self.scroll_to_element(MiniCart.NoTip)
        self.click(MiniCart.NoTip)

    def click_Tip5(self):
        self.scroll_to_element(MiniCart.Tip5)
        self.click(MiniCart.Tip5)

    def click_Tip10(self):
        self.scroll_to_element(MiniCart.Tip10)
        self.click(MiniCart.Tip10)

    def click_Tip15(self):
        self.scroll_to_element(MiniCart.Tip15)
        self.click(MiniCart.Tip15)

    def click_Tip20(self):
        self.scroll_to_element(MiniCart.Tip20)
        self.click(MiniCart.Tip20)

    def click_changeAddress(self):
        self.scroll_to_element(MiniCart.ChangeAddress)
        # self.wait_for_page_load(20)
        # self.wait_for_presence(MiniCart.ChangeAddress, 30)
        self.click(MiniCart.ChangeAddress)

    def click_Cross(self):
        self.click(MiniCart.clickCross)

    def enter_notes(self, notes):
        self.scroll_to_element(MiniCart.Notes_text)
        self.find_elements(MiniCart.Notes_text).clear()
        self.find_element(MiniCart.Notes_text).send_keys(notes)

    def click_payment(self):
        self.scroll_to_element(MiniCart.Payment)
        self.scroll_to(1653, 1006)
        # self.wait_for_loader(15)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(MiniCart.Payment))
        element.click()
        # self.wait_for_loader(1)
        # self.click(MiniCart.ProceedToPayment)

    def click_apply(self):
        self.scroll_to_element(MiniCart.Apply)
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(MiniCart.Apply)).click()
        self.click(MiniCart.Apply)

    def click_paypal(self):
        # self.wait_for_loader(15)
        self.click(MiniCart.paypal)

    def click_SignIn(self):
        self.click(MiniCart.signIn)

    def click_ShopNow(self):
        self.click(MiniCart.shopNow)

    def click_Grocery(self):
        self.click(MiniCart.clickGrocery)

    def click_SecondShop(self):
        self.click(MiniCart.secondShop)

    def select_dropdown(self):
        # self.select(MiniCart.yourAccount, "Sign In")
        self.click(MiniCart.yourAccount)

    def click_changeMethod(self):
        # self.scroll_to_element(MiniCart.ChangePaymentMethod)
        # self.wait_for_page_load(15)
        self.click(MiniCart.ChangePaymentMethod)

    def click_Addmethod(self):
        self.click(MiniCart.AddPaymentMethod)

    def EnterCardNumber(self, credit):
        self.find_elements(MiniCart.CreditCardNumber).clear()
        self.find_element(MiniCart.CreditCardNumber).send_keys(credit)

    def EnterExpiry(self, expiration):
        self.find_elements(MiniCart.Expiration).clear()
        self.find_element(MiniCart.Expiration).send_keys(expiration)

    def EnterCVV(self, Cvv):
        self.find_elements(MiniCart.CVV).clear()
        self.find_element(MiniCart.CVV).send_keys(Cvv)

    def click_Pay(self):
        self.click(MiniCart.Pay)

    def deliveryLabel(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(MiniCart.DeliveryLabel))

    def click_payment1(self):
        self.scroll_to_element(MiniCart.Payment)
        self.scroll_to(1653, 1048)
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable(MiniCart.Payment))
        element.click()

    def click_Department(self):
        self.click(MiniCart.Department)

    def click_ShopByGrocery(self):
        self.click(MiniCart.GroceryShop)



