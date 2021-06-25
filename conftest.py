# !/usr/bin/python
# --*-- coding:utf-8 --*--
from datetime import datetime

import pytest
import webbrowser

from selenium.webdriver.chrome import options
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():

    driver = webdriver.Chrome('resources//chromedriver.exe', options=options)
    driver.get('http://www.gogle.com')
    driver.implicitly_wait(5)

    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.dev.quicklly.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure

            extra.append(pytest_html.extras.image('/home/excellence/PycharmProjects/gitAutomation/tests/screenshots/f"screenshot{name}.png"'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra