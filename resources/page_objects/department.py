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
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/header/div[3]/span')
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.yourAccount)).click()

    def click_signin(self):
        element = self.driver.find_element_by_xpath('//*[@id="procedcheckoutBtn"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.scroll_to_element(Department.SignInButton)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.SignInButton)).click()

        # self.click(Department.SignInButton)

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
        # self.click(Department.proceed_to_checkOut)
        element = self.driver.find_element_by_id('lnkProceedToCheckout')
        self.driver.execute_script("arguments[0].click();", element)

    def click_payment1(self):
        # self.scroll_to_element(Department.payment)
        element = self.driver.find_element_by_id('proceedtopayment')
        self.driver.execute_script("arguments[0].click();", element)

    def click_additem(self):
        self.scroll_to_element(Department.additem)
        element = self.driver.find_element_by_xpath('//*[@id="img_270"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Pay(self):
        self.click(Department.Pay)

    def click_InstantPot(self):
        self.click(Department.Pot)

    def click_Department(self):
        self.click(Department.Department)

    def click_select(self):
        self.scroll_to_element(Department.select)
        WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located(Department.select))
        element = self.driver.find_element_by_xpath('//*[@id="nationwide"]/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Add(self):
        self.scroll_to_element(Department.Add)
        WebDriverWait(self.driver, self.wait).until(EC.visibility_of_element_located(Department.Add))
        element = self.driver.find_element_by_xpath('//*[@id="img_77024"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCart(self):
        self.click(Department.AddToCart)

    def click_quicklly(self):
        element = self.driver.find_element_by_xpath('/html/body/header/a/img')
        self.driver.execute_script("arguments[0].click();", element)
        # WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.quicklly)).click()
        # self.click(Department.quicklly)

    def click_seeti(self):
        self.click(Department.Seeti)

    def click_rightArrow(self):
        self.click(Department.right_arrow)

    def click_remove(self):
        self.click(Department.delete)

    def click_fresh(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.GoFresh)).click()

    def click_ADDLG(self):
        self.click(Department.AddToCartLG)

    def click_addPotato(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_51875"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartPotato(self):
        self.click(Department.AddToCartP)

    def click_food(self):
        self.click(Department.food)

    def click_MakkiFood(self):
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_addTenders(self):
        self.scroll_to_element(Department.AddTenders)
        element = self.driver.find_element_by_xpath('//*[@id="load_data"]/div[2]/div/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartTenders(self):
        self.click(Department.TendersAddToCart)

    def click_submitTenders(self):
        self.click(Department.submitTenders)

    def click_BBQ(self):
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[9]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_TikkaImage(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_132523"]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.chickenTikkaImage)

    def click_AddChickenTikkaToCart(self):
        self.click(Department.AddTikkaToCart)

    def click_Catering(self):
        self.click(Department.Catering)

    def click_Hyderabad(self):
        element = self.driver.find_element_by_xpath('//*[@id="Catering"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddBeef(self):
        self.scroll_to_element(Department.AddBeefFry)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[5]/div/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartBeef(self):
        self.click(Department.AddToCartBeef)

    def Submit_Beef(self):
        self.click(Department.submitBeef)

    def click_mealBasket(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.mealBasket)).click()

    def select_mealPlan(self):
        self.scroll_to_element(Department.MealPlan)
        element = self.driver.find_element_by_xpath('//*[@id="meal-basket"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Korma(self):
        self.scroll_to_element(Department.AddKorma)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def Plus_Korma(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div[1]/div[1]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartCK(self):
        self.click(Department.AddToCartCK)

    def click_Tiffin(self):
        self.click(Department.TiffinServices)

    def click_Chicago(self):
        element = self.driver.find_element_by_xpath('//*[@id="tiffin-services"]/div/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def select_VegThali(self):
        element = self.driver.find_element_by_xpath('//*[@id="TiffinServices"]/div[2]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartVT(self):
        self.click(Department.AddToCartVegThali)

    def submitVT(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.submitVT)).click()

    def click_MealKit(self):
        # self.click(Department.MealKit)
        self.driver.implicitly_wait(20)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[10]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def select_MealPlan20(self):
        self.scroll_to_element(Department.selectMealKit)
        element = self.driver.find_element_by_css_selector('#meal-kit > div.clsSlider > div:nth-child(1) > form > a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_CuminCLub(self):
        element = self.driver.find_element_by_xpath('//*[@id="home"]/div/div[4]/div/a/div/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Papad(self):
        element = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div[3]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)

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

    def click_TickBox(self):
        self.scroll_to_element(Department.clickTick)
        element = self.driver.find_element_by_xpath('//*[@id="flexCheckDefault"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_RightArrow(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[5]/div/div/i[2]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.clickRA)

    def click_OrganicGrocery(self):
        self.driver.implicitly_wait(30)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[8]/img')
        self.driver.execute_script("arguments[0].click();", element)

    def click_BuildBox(self):
        self.scroll_to_element(Department.BuildABox)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddJowar(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[3]/div/div[1]/div[3]/div[1]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartJowar(self):
        self.click(Department.AddToCartOrganic)

    def click_LeftArrow(self):
        self.click(Department.LeftArrow)

    def click_rotiKit(self):
        WebDriverWait(self.driver, self.wait).until(EC.element_to_be_clickable(Department.rotiKIt)).click()

    def click_RotiBox(self):
        self.scroll_to_element(Department.buildRotiBox)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddWholeWheatRoti(self):
        self.scroll_to_element(Department.AddWholeWheatRoti)
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[2]/div[3]/div/div[1]/div[3]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartRoti(self):
        element = self.driver.find_element_by_xpath('//*[@id="searchhide"]/div[3]/div/div/div[3]/button')
        self.driver.execute_script("arguments[0].click();", element)

    def click_Checkout2(self):
        self.click(Department.checkout2)

    def click_Liquor(self):
        self.click(Department.liquorStore)

    def click_beer(self):
        self.click(Department.Beer)

    def click_classicLime(self):
        element = self.driver.find_element_by_xpath('//*[@id="img_138002"]')
        self.driver.execute_script("arguments[0].click();", element)

    def click_AddToCartBeer(self):
        self.click(Department.AddToCartBeer)

    def click_ChaiAndCoffee(self):
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div/div/div/a[4]/img')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.ChaiAndCoffee)

    def click_ChaiBox(self):
        element = self.driver.find_element_by_xpath('/html/body/div[4]/section[1]/div/div/div[2]/div[4]/form/button')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.ChaiBox)

    def AddKimbala(self):
        element = self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div[1]/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.AddKimbala)

    def click_NationWideShop(self):
        self.click(Department.NationWideShop)

    def click_IndianMealKit(self):
        self.click(Department.IndianMealKit)

    def click_SelectProducts(self):
        element = self.driver.find_element_by_xpath('/html/body/div[4]/section[1]/div/div/div[1]/div/div[5]/form/button')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.SelectProducts)

    def click_AddMixVegetable(self):
        self.click(Department.AddMixVegetable)

    def click_AddMisalPav(self):
        self.click(Department.AddMisalPav)

    def click_PlusMixVegetable(self):
        self.click(Department.PlusMixVegetable)

    def click_AddToCartNW(self):
        self.click(Department.AddToCartNW)

    def click_Methai(self):
        self.click(Department.MethaiPaneer)

    def click_DalTadka(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[4]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.DalTadka)

    def click_plusDalTadka(self):
        element = self.driver.find_element_by_xpath(
            '/html/body/div[5]/section[3]/div/div/div[1]/div[4]/div[3]/p/a/span[3]')
        self.driver.execute_script("arguments[0].click();", element)
        # self.click(Department.PlusDalTadka)

