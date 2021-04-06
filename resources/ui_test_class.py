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

    forgot_page: BasePage = None

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
