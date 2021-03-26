#!/usr/bin/env python
from common import env
import sys


class DataClass:

    CHROME_DRIVER_PATH_UBUNTU = 'chromedriver'
    CHROME_DRIVER_PATH_WINDOWS = 'chromedriver.exe'
    BASE_URL = env.get_config_value('portal_ui', 'base_url')


    PAGE_TITLE = 'Quicklly'
    ERROR_PAGE_TITLE = 'Privacy error'

    if sys.platform == 'win32':
        platform = 'windows'
    else:
        platform = 'linux'


