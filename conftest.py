# !/usr/bin/python
# --*-- coding:utf-8 --*--
import pytest
from py._xmlgen import html
from datetime import datetime


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Tester: xqc")])


def pytest_configure(config):
    config._metadata['Test Address'] = 'https://10.12.104.18'


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    # cells.insert(1,html.th("Test_nodeid"))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    # cells.insert(1,html.td(report.nodeid))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     timestamp = datetime.now().strftime('%H-%M-%S')
#
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#
#         feature_request = item.funcargs['request']
#
#         driver = feature_request.getfuncargvalue('browser')
#         driver.save_screenshot('D:/report/scr' + timestamp + '.png')
#
#         extra.append(pytest_html.extras.image('D:/report/scr' + timestamp + '.png'))
#
#         # always add url to report
#         extra.append(pytest_html.extras.url('http://www.example.com/'))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.image('D:/report/scr.png'))
#             extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#         report.extra = extra
