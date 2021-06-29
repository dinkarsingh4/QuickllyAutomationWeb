from selenium.webdriver.remote.webelement import WebElement

from resources.config_methods import DataClass
from resources.locators import Department
from resources.page_objects.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dept(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DataClass.BASE_URL)

    def zip(self, zipcode):
        self.find_elements(Department.enter_zip).clear()
        self.find_element(Department.enter_zip).send_keys(zipcode)

    def submit_zip(self):
        self.click(Department.submit_zip)

    def select_dropdown(self):
        # element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        # self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.yourAccount)).click()

        # self.click(Department.yourAccount)

    def click_signin(self):
        self.scroll_to_element(Department.SignInButton)
        self.click(Department.SignInButton)

    def EnterEmail(self, email):
        self.find_elements(Department.Email).clear()
        self.find_element(Department.Email).send_keys(email)

    def EnterPass(self, password):
        self.find_elements(Department.Pass).clear()
        self.find_element(Department.Pass).send_keys(password)

    def click_login(self):
        self.click(Department.LoginButton)

    def click_MiniCart1(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_MiniCart(self):
        element = self.driver.find_element_by_xpath('/html/body/header/div[4]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout(self):
        self.click(Department.proceed_to_checkOut)

    def click_payment1(self):
        self.scroll_to_element(Department.payment)
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_additem(self):
        self.scroll_to_element(Department.additem)
        element = self.driver.find_element_by_xpath('//*[@id="img_270"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(Department.Pay)

    def click_InstantPot(self):
        # WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(Department.Pot))
        # element = self.driver.find_element_by_xpath('/html/body/header/div[2]/div/div[1]/div[1]/div/div/ul/li[8]/a')
        # self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.Pot)).click()
        # self.click(Department.Pot)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.Pot)).click()

    def click_Department(self):
        self.click(Department.Department)

    def click_select(self):
        self.scroll_to_element(Department.select)
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(Department.select))
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Add(self):
        self.scroll_to_element(Department.Add)
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(Department.Add))
        # WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(Department.Add))
        # self.click(Department.Add)
        element = self.driver.find_element_by_xpath('//*[@id="img_76996"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        self.click(Department.AddToCart)

    def click_quicklly(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.quicklly)).click()
        # self.click(Department.quicklly)

    def click_seeti(self):
        self.click(Department.Seeti)

    def click_rightArrow(self):
        self.click(Department.right_arrow)

    def click_remove(self):
        self.click(Department.delete)

    def click_fresh(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.GoFresh)).click()
        # self.click(Department.GoFresh)

    def click_ADDLG(self):
        self.click(Department.AddToCartLG)

    def click_addPotato(self):
        self.click(Department.addSecondItem)

    def click_AddToCartPotato(self):
        self.click(Department.AddToCartP)

    def click_food(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.food)).click()

    def click_MakkiFood(self):
        self.click(Department.MakkiFastFood)

    def click_addTenders(self):
        self.scroll_to_element(Department.AddTenders)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.AddTenders)

    def click_AddToCartTenders(self):
        self.click(Department.TendersAddToCart)

    def click_submitTenders(self):
        self.click(Department.submitTenders)

    def click_BBQ(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[4]/div/div/div/div/a[4]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.BBQKit)

    def click_TikkaImage(self):
        self.click(Department.chickenTikkaImage)

    def click_AddChickenTikkaToCart(self):
        self.click(Department.AddTikkaToCart)

    def click_Catering(self):
        self.click(Department.Catering)

    def click_Hyderabad(self):
        # self.click(Department.HyderabadHouse)
        element = self.driver.find_element_by_xpath('//*[@id="Catering"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBeef(self):
        self.scroll_to_element(Department.AddBeefFry)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[4]/div/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartBeef(self):
        self.click(Department.AddToCartBeef)

    def Submit_Beef(self):
        self.click(Department.submitBeef)

    def click_mealBasket(self):
        self.click(Department.mealBasket)

    def select_mealPlan(self):
        self.scroll_to_element(Department.MealPlan)
        element = self.driver.find_element_by_xpath('//*[@id="meal-basket"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.MealPlan)

    def click_Korma(self):
        self.scroll_to_element(Department.AddKorma)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def Plus_Korma(self):
        # self.click(Department.plusKorma)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.plusKorma)).click()
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartCK(self):
        self.click(Department.AddToCartCK)

    def click_Tiffin(self):
        self.click(Department.TiffinServices)

    def click_Chicago(self):
        self.click(Department.ChicagoTiffin)

    def select_VegThali(self):
        self.click(Department.VegThali)

    def click_AddToCartVT(self):
        self.click(Department.AddToCartVegThali)

    def submitVT(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.submitVT)).click()
        # self.click(Department.submitVT)

    def click_MealKit(self):
        self.click(Department.MealKit)

    def select_MealPlan20(self):
        # self.click(Department.selectMealKit)
        self.scroll_to_element(Department.selectMealKit)
        element = self.driver.find_element_by_xpath('//*[@id="meal-kit"]/div[2]/div[1]/form/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CuminCLub(self):
        self.click(Department.CuminClub)

    def click_Papad(self):
        self.click(Department.AddPapad)

    def Plus_Papad(self):
        self.click(Department.plusPapad)

    def click_AddToCartPapad(self):
        self.click(Department.AddToCartPapad)

    def click_Recipes(self):
        self.click(Department.Recipes)

    def click_PalakPaneer(self):
        self.click(Department.PalakPaneer)

    def click_AddToBasket(self):
        self.scroll_to_element(Department.AddToBasket)
        element = self.driver.find_element_by_xpath('//*[@id="addchekListprodct"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Delivery(self):
        self.click(Department.delivery)

    def click_timeOfDelivery(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.timeDelivery)).click()
        # self.click(Department.timeDelivery)

    def click_TickBox(self):
        self.scroll_to_element(Department.clickTick)
        element = self.driver.find_element_by_xpath('//*[@id="flexCheckDefault"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        self.click(Department.clickRA)

    def click_OrganicGrocery(self):
        self.click(Department.OrganicGrocery)

    def click_BuildBox(self):
        self.scroll_to_element(Department.BuildABox)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddJowar(self):
        self.click(Department.AddOrganicJowar)

    def click_AddToCartJowar(self):
        self.click(Department.AddToCartOrganic)



