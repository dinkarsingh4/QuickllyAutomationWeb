#!/usr/bin/env python

import unittest
import pprint
import time
from resources.config_methods import DataClass
from resources.common_methods import Common

from resources.page_objects.base_page import BasePage
from resources.page_objects.LogIn import Login
from resources.page_objects.guest import guest
from resources.page_objects.needaccount import needanaccount
from resources.page_objects.forgetpassword import forgetpass
from resources.page_objects.cart import Cart
from resources.page_objects.eVoucher import evoucher
from resources.page_objects.department import Dept
from resources.page_objects.Zipcodes import Zip
from resources.page_objects.contact_us import contactUs
from selenium.webdriver import Remote


# from client.auto_it_methods import AutoIt


class UIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    base_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIClass, cls).setUpClass()
        cls.base_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.base_page.get_browser_instance()
        cls.base_page.driver = cls.driver
        cls.maine_page = Login(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIClass, cls).tearDownClass()


class UIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    guest_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIIClass, cls).setUpClass()
        cls.guest_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.guest_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.guest_page.driver = cls.driver
        cls.guest_page = guest(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIIClass, cls).tearDownClass()


class UIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    need_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIIIClass, cls).setUpClass()
        cls.need_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.need_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.need_page.driver = cls.driver
        cls.need_page = needanaccount(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIIIClass, cls).tearDownClass()


class UIIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    forget_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UIIIIClass, cls).setUpClass()
        cls.forget_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.forget_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.forget_page.driver = cls.driver
        cls.forget_page = forgetpass(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UIIIIClass, cls).tearDownClass()


class UVClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    cart_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVClass, cls).setUpClass()
        cls.cart_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.cart_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.cart_page.driver = cls.driver
        cls.cart_page = Cart(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVClass, cls).tearDownClass()


class UVIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    eVoucher_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIClass, cls).setUpClass()
        cls.eVoucher_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.eVoucher_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.eVoucher_page.driver = cls.driver
        cls.eVoucher_page = evoucher(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVIClass, cls).tearDownClass()


class UVIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    depart_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIIClass, cls).setUpClass()
        cls.depart_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.depart_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.depart_page.driver = cls.driver
        cls.depart_page = Dept(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        super(UVIIClass, cls).tearDownClass()


class UVIIIClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    zip_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIIIClass, cls).setUpClass()
        cls.zip_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.zip_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.zip_page.driver = cls.driver
        cls.zip_page = Zip(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVIIIClass, cls).tearDownClass()


class UVIXClass(unittest.TestCase):
    aut_prefix = 'automation_'
    driver: Remote = None
    const_data = DataClass

    contact_page: BasePage = None

    @classmethod
    def setUpClass(cls):
        super(UVIXClass, cls).setUpClass()
        cls.contact_page = BasePage(cls.driver)
        cls.common_methods = Common(cls.driver)
        cls.driver = cls.contact_page.get_browser_instance()
        cls.base_page = BasePage(cls.driver)
        cls.contact_page.driver = cls.driver
        cls.contact_page = contactUs(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super(UVIXClass, cls).tearDownClass()


    @classmethod
    def login(cls):
        pass

    # return cls.login_page.login(cls.login_page.admin_user, cls.login_page.admin_password)

    @classmethod
    def logout(cls):
        pass

    # return cls.home_page.logout()

    @staticmethod
    def display_bug(_id, desc=None):
        if desc:
            print(desc)
            print('bug link{}'.format(_id))

    @staticmethod
    def pprint(arg):
        print(pprint.pformat(arg))

    @staticmethod
    def sleep(arg):
        time.sleep(arg)
