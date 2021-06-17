# !/usr/bin/python
# --*-- coding:utf-8 --*--


from py._xmlgen import html
from datetime import datetime
import pytest
import os
from selenium import webdriver
import pytest
driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="file:/C:/SeleniumProject/Pytest_HTML_ScreenShot/ScreenShots/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file("/home/excellence/PycharmProjects/gitAutomation/screenshots"+name)
    # driver.get_screenshot_as_file(name)



@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
    return driver

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     driver = None
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == 'setup':
#         xfail = hasattr(report, 'wasxfail')
#
#
#         if (report.skipped and xfail) or (report.failed and not xfail):
#
#             screenshot = driver.get_screenshot_as_base64()
#             extra.append(pytest_html.extras.image(screenshot, ''))
#         report.extra = extra



# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th("Description"))
#     cells.insert(1, html.th("Time", class_="sortable time", col="time"))
#     cells.pop()
#
#
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
#     cells.pop()
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)

#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         # always add url to report
#
#         extra.append(pytest_html.extras.url('http://www.dev.quicklly.com/'))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.image('screenshots'))
#             extra.append(pytest_html.extras.html('<div>djndjnk.fn</div>'))
#         report.extra = extra
#         report.description = str(item.function.__doc__)


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Description'))
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
