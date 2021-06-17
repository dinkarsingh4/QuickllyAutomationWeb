# !/usr/bin/python
# --*-- coding:utf-8 --*--


from py._xmlgen import html
from datetime import datetime
import pytest
import os


@pytest.fixture(params=(1, 2, 3))
def pytest_runtest_makereport(item, call):

    timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':

        feature_request = item.funcargs['request']

        driver = feature_request.getfuncargvalue('browser')
        driver.save_screenshot('/home/excellence/PycharmProjects/gitAutomation/screenshots'+timestamp+'.png')

        extra.append(pytest_html.extras.image('/home/excellence/PycharmProjects/gitAutomation/screenshots'+timestamp+'.png'))

        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.image('/home/excellence/PycharmProjects/gitAutomation/screenshots'))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra

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
